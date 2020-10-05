from mycroft import MycroftSkill, intent_handler
from mycroft.configuration import Configuration
from mycroft.skills.context import adds_context, removes_context
from adapt.intent import IntentBuilder


class SetMyNameSkill(MycroftSkill):
    # variabile di classe per il salvataggio del nome
    info = {
        'name': ""
    }

    new_name_regex = ''

    reset = False
    retry = False

    ''' costruttore '''

    def __init__(self):
        MycroftSkill.__init__(self)

    '''' operazioni di inizializzazione della classe '''

    def initialize(self):
        # legge il dato 'nome_utente' dal file di configurazione
        self.info['name'] = self.config_core['user_name']
        if self.info['name'] == "" or self.info['name'] == '' :
            self.info['name'] = None 

    #TODO; implementare con regex. NameRegex non funziona
    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola di quelle indicate nel file 'Callme.voc'.
        Questo intent si occupa di gestire le operazioni preliminare per il settaggio o il resettaggio del nome.
        Questo intent si attiva se l'utente pronuncia '... chiamami {nome}' es. "per favore chiamami Dario" 
        Il nome deve essere la parola subito successiva alla parola 'chiamami', inoltre dopo il nome non deve seguire alcuna parola es. 'chiamami Dario perfavore' 
        settera' il nome a 'Dario perfavore'  '''
    @intent_handler(IntentBuilder('SetMyNameRegex').require('Callme').optionally('NameRegex'))
    def handle_set_my_name_regex__intent(self, message):
        # logger
        self.log.info("set my name regex intent")
        #TODO: cambiare slpit utilizzando le regex
        #salva il nome pronunciato dall'utente. il nome e' la parola che segue Dario.
        self.new_name_regex = message.data.get('utterance').split('chiamami')[1]
        #logger
        self.log.info(self.new_name_regex)
        self.log.info(message.data)
        # se il nome non e ancora stato settato o e stato resettato o si ta riprovando 
        if not self.is_setUpAlreadyAName() or self.reset or self.retry  :
            # logger
            self.log.info("set my name intent, there is not a name setted")
            # chiede all'utente se il nome compreso e' corretto ed attende per una risposta
            self.info['name'] = self.new_name_regex
            self.speak_dialog('set.name.correctness', self.info,
                              expect_response=True, wait=True)
            # imposta il contesto a 'SetNameContext'
            self.set_context('SetNameContext')
        # se il nome e gia stato impostato
        else:
            # logger
            self.log.info(
                "set my name intent, there is a name setted, calling another intent")
            # imposta il contesto a 'ChangeNameRegexContext'
            self.set_context('ChangeNameRegexContext')
            # chiama la funzione che si occupa di gestire il reset del nome
            self.handle_change_name_intent_regex(message)


    
    ''' Per l'esecuzione di questo intent e' necessario che il contesto sia settato a 'ChangeNameRegexContext'
    Questo intent si occupa di gestire il reset del nome. Chiede all'utente se vuole davvero cambiare il nome e attende per una risposta. 
    Si attiva solo se chiamato da handle_set_my_name_regex__intent'''
    @intent_handler(IntentBuilder('ChangeMyNameRegex').require('ChangeNameRegexContext').build())
    def handle_change_name_intent_regex(self, message):
        # logger
        self.log.info("change my name regex intent ")
        # chiede all'utente la conferma dell'operazione di reset ed attende per una risposta
        self.speak('Avevi scelto come nome {}. Vuoi Cambiarlo con {} ?'.format(self.info['name'], self.new_name_regex), expect_response = True, wait= True)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameYes.voc' e che il contesto sia settato a 'SetNameRegexContext'.
        Questo intent si occupa di gestire la conferma della volonta' di cambiare il nome.'''
    @intent_handler(IntentBuilder('YesCorrectnessRegex').require('SetMyNameYes').require('ChangeNameRegexContext').build())
    def handle_yes_correctness_regex_intent(self, message):
        # logger
        self.log.info("yes correctness regex intent")
        #setta il nuovo nome
        self.info['name'] = self.new_name_regex
        # salva il nuovo nome nel file userinfo.config e ricarica i file di configurazione in memoria
        Configuration.update_user_info('user_name', self.info['name'])
        # conferma dell'avvenuto settaggio/resettaggio del nome
        self.speak_dialog('ok.i.call.u', self.info)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameNo.voc' e che il contesto sia settato a 'ChangeNameRegexContext'.
        Questo intent si occupa di gestire la disconferma dell'operazione di reset del nome'''
    @intent_handler(IntentBuilder('NoChangeRegex').require('SetMyNameNo').require('ChangeNameRegexContext').build())
    def handle_change_name_no_regex_intent(self, message):
        # logger
        self.log.info("don't change my name regex intent")
        # mycroft conferma che continuera a chiamare l'utente con il nome che era stato settato in origine
        self.speak_dialog("dont.change.my.name", self.info)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'Dont.voc' ed una indicata nel file 'Understand.voc' e che il contesto sia settato a 'SetNameContext'.
    Questo intent si occupa di gestire la non comprensione di quello che sta accadendo da parte dell'utente
    Questo intent si attiva nel momento in cui chiesto se si vuole reimpostare il nome l'utente risponde con 'non ho capito'. '''
    
    @intent_handler(IntentBuilder('DontUnderstandChangeRegex').require('Dont').require('Understand').require('ChangeNameRegexContext').build())
    def handle_dont_understand_change_name_regex_intent(self, message):
        # logger
        self.log.info("dont_understand_change_name_regex")
        # spiegazione di quello che sta accadendo
        self.speak('mi hai chiesto di chiamarti {}'.format(self.new_name_regex))
        self.speak('ma avevo imparato a chiamarti {}'.format(self.info['name']))
        self.speak('vuoi che da oggi ti chiami {} ?'.format(self.new_name_regex), expect_response = True, wait = True)
     

    
    
    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola di quelle indicate nel file 'Name.voc' e
        o una parola di quelle indicate nel file 'Set.voc' o una parola di quelle indicate nel file 'Change.voc'.
        Questo intent si occupa di gestire el operazioni preliminare per il settaggio o il resettaggio del nome.
        Questo intent si attiva quando l'utente pronuncia una frase tipo 'cambia il mio nome' o 'impara il mio nome' '''
    
    @intent_handler(IntentBuilder('SetMyName').require('Name').one_of('Set', 'Change'))
    def handle_set_my_name_intent(self, message):
        # logger
        self.log.info("set my name intent")
        # se il nome non e ancora stato settato o e stato resettato
        if not self.is_setUpAlreadyAName() or self.reset or self.retry:
            # logger
            self.log.info("set my name intent, there is not a name setted")
            # chiede all'utente come vuole essere chiamato e salva la risposta
            # TODO: aggiungere flow per il 'non ho capito' a questo punto della conversazione
            self.info['name'] = self.get_response('set.name')
            # chiede all'utente se il nome compreso e' corretto ed attende per una risposta
            self.speak_dialog('set.name.correctness', self.info,
                              expect_response=True, wait=True)
            # imposta il contesto a 'SetNameContext'
            self.set_context('SetNameContext')
        # se il nome e gia stato impostato
        else:
            # logger
            self.log.info(
                "set my name intent, there is a name setted, calling another intent")
            # imposta il contesto a 'ChangeNameContext'
            self.set_context('ChangeNameContext')
            # chiama la funzione che si occupa di gestire il reset del nome
            self.handle_change_name_intent(message)


    





    ''' Per l'esecuzione di questo intent e necessario che il contesto sia settato a 'ChangeNameContext'
        Questo intent si occupa di gestire il reset del nome
        Chiede all'utente se vuole cambiare il nome gia' salvato e attende per una risposta '''
    @intent_handler(IntentBuilder('ChangeMyName').require('ChangeNameContext').build())
    def handle_change_name_intent(self, message):
        # logger
        self.log.info("change my name intent")
        # chiede all'utente la conferma dell'operazione di reset ed attende per una risposta
        self.speak_dialog('change.name', self.info,
                          expect_response=True, wait=True)





    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameYes.voc' e che il contesto sia settato a 'ChangeNameContext'.
        Questo intent si occupa di gestire la conferma dell'operazione di reset del nome '''

    @intent_handler(IntentBuilder('YesChange').require('SetMyNameYes').require('ChangeNameContext').build())
    def handle_change_name_yes_intent(self, message):
        # logger
        self.log.info("yes change my name intent")
        # conferma
        self.speak("Va bene")
        # impostazione del Flag per il reset del nome
        self.reset = True
        # rimozione del contesto 'ChangeNameContext'
        self.remove_context('ChangeNameContext')
        # chiamata dell'handler che si occupa della gestione dell'impostazione del nome.
        self.handle_set_my_name_intent(message)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameNo.voc' e che il contesto sia settato a 'ChangeNameContext'.
        Questo intent si occupa di gestire la disconferma dell'operazione di reset del nome 
        Quando l'utente risponde negativamente alla richiesta di conferma di cambiamento del nome. es. mycroft:'avevi scelto {nome}, vuoi cambiarlo?' user:'No' '''
    @intent_handler(IntentBuilder('NoChange').require('SetMyNameNo').require('ChangeNameContext').build())
    def handle_change_name_no_intent(self, message):
        # logger
        self.log.info("don't change my name intent")
        # mycroft conferma che continuera a chiamare l'utente con il nome che era stato settato in origine
        self.speak_dialog("dont.change.my.name", self.info)
        #resetto le variabili 
        self.re_set()

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameYes.voc' e che il contesto sia settato a 'SetNameContext'.
        Questo intent si occupa di gestire la conferma della correttezza del nome capito da mycroft
        Quando l'utente risponde positivamente alla richiesta di conferma di cambiamento del nome. es. mycroft:'avevi scelto {nome}, vuoi cambiarlo?' user:'Si' '''
    @intent_handler(IntentBuilder('YesCorrectness').require('SetMyNameYes').require('SetNameContext').build())
    def handle_yes_correctness_intent(self, message):
        # logger
        self.log.info("yes correctness intent")
        # salva il nuovo nome nel file userinfo.config e ricarica i file di configurazione in memoria
        Configuration.update_user_info('user_name', self.info['name'])
        # resetta i flag ai valori iniziali
        self.re_set()
        # conferma dell'avvenuto settaggio/resettaggio del nome
        self.speak_dialog('ok.i.call.u', self.info)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameNo.voc' e che il contesto sia settato a 'SetNameContext'.
        Questo intent si occupa di gestire la NON conferma della correttezza del nome capito da mycroft
        Quando l'utente risponde negativamente alla richiesta di corretteza del nome compreso. es. mycroft:'vuoi che ti chiami {nome} ?' user:'No' '''

    @intent_handler(IntentBuilder('NoCorrectness').require('SetMyNameNo').require('SetNameContext').build())
    def handle_no_correctness_intent(self, message):
        # logger
        self.log.info("no correctness intent")
        # rimuove il contesto 'SetNameContext'
        self.remove_context('SetNameContext')
        # setta il contesto a 'NoCorrectnessContext'
        self.set_context('NoCorrectnessContext')
        # chiede se si vuole ritentare il settaggio del nome ed attende per una risposta
        self.speak('Vuoi riprovare?', expect_response=True, wait=True)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameYes.voc' e che il contesto sia settato a 'NoCorrectnessContext''.
    Questo intent si occupa di gestire la conferma del voler ritentare il settaggio del nome.
    Come si puo notare questo intent si attivera solo dopo l'esecuzione dell'intent 'handle_no_correctness_intent' e solo ad una risposta affermativa dell'utente
    Quando l'utente risponde positvamente alla richiesta di voler riprovare. es. mycroft:'vuoi riprovare ?' user:'Si' '''

    @intent_handler(IntentBuilder('YesRetry').require('SetMyNameYes').require('NoCorrectnessContext').build())
    def handle_yes_retry(self, message):
        # logger
        self.log.info("yes retry intent")
        # resetta il flaf
        self.retry = True
        # conferma che si sta riprovando a settare il nome
        self.speak_dialog('set.name.retry')
        # rimuove il contesto 'NoCorrectnessContext'
        # a questo punto, si ricomincia dall'inizio quindi nessun contesto e necessario
        self.remove_context('NoCorrectnessContext')
        # richiama la funzione che si occupa di settare il nome
        self.handle_set_my_name_intent(message)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'SetMyNameNo.voc' e che il contesto sia settato a 'NoCorrectnessContext''.
    Questo intent si occupa di gestire la NON conferma del voler ritentare il settaggio del nome.
    Come si puo notare questo intent si attivera solo dopo l'esecuzione dell'intent 'handle_no_correctness_intent' e solo ad una risposta affermativa dell'utente
    Quando l'utente risponde negativamente alla richiesta di voler riprovare. es. mycroft:'vuoi riprovare ?' user:'No' '''

    @intent_handler(IntentBuilder('NoRetry').require('SetMyNameNo').require('NoCorrectnessContext').build())
    def handle_no_retry(self, message):
        # logger
        self.log.info("no retry intent")
         # resettiamo la variabile di classe al nome indicato nel file
        self.info['name'] = self.config_core['user_name']
        self.log.info(self.config_core['user_name'])
        self.log.info(self.is_setUpAlreadyAName())
        # risposta se un nome era gia presente un nome per l'utente
        if self.is_setUpAlreadyAName():
            # conferma del non avvenuto cambiamento
            self.speak_dialog("dont.change.my.name", self.info)
        # risposta se non era presente un nome per l'utente
        else:
            self.speak('Va bene, imparerò il tuo nome la prossima volta')
        self.re_set()

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'Dont.voc' ed una indicata nel file 'Understand.voc' e che il contesto sia settato a 'SetNameContext'.
        Questo intent si occupa di gestire la non comprensione di quello che sta accadendo da parte dell'utente
        Questo intent si attiva nel momento in cui chiesto se si vuole riprovare a impostare il nome l'utente risponde con 'non ho capito'. '''
    @intent_handler(IntentBuilder('DontUnderstandRetry').require('Dont').require('Understand').require('NoCorrectnessContext').build())
    def handle_dont_understand_no_correctness_intent(self, message):
        # logger
        self.log.info("dont_understand_no_correctness")
        # spiegazione di quello che sta accadendo
        self.speak('Sto cercando di imparare il tuo nome')
        self.speak('Ho capito che vorresti che io ti chiamassi: {}'.format(
            self.info['name']))
        self.speak('Ma mi hai detto che non e corretto')
        self.handle_no_correctness_intent(message)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'Dont.voc' ed una indicata nel file 'Understand.voc' e che il contesto sia settato a 'ChangeNameContext'.
        Questo intent si occupa di gestire la non comprensione di quello che sta accadendo da parte dell'utente.
        Questo intent si attiva nel momento in cui chiesto se si vuole procedere al reset del nome l'utente risponde con 'non ho capito'. '''
    @intent_handler(IntentBuilder('DontUnderstandChangeMyName').require('Dont').require('Understand').require('ChangeNameContext').build())
    def handle_dont_understand_change_name_intent(self, message):
        # logger
        self.log.info("dont_understand_change_name_intent")
        # spiegazione di quello che sta accadendo
        self.speak('Mi hai chiesto di imparare un nome per te')
        self.speak('L\'ultima volta mi hai chiesto di chiamarti: {}'.format(
            self.info['name']))
        self.speak('Vuoi cambiarlo?', expect_response=True, wait=True)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'Dont.voc' ed una indicata nel file 'Understand.voc' e che il contesto sia settato a 'SetNameContext'
        Questo intent si occupa di gestire la non comprensione di quello che sta accadendo da parte dell'utente.
        Questo intent si attiva nel momento in cui chiesto se il nome è corretto l'utente risponde con 'non ho capito'. '''
    @intent_handler(IntentBuilder('DontUnderstandCorrectness').require('Dont').require('Understand').require('SetNameContext').build())
    def handle_dont_understand_correctness(self, message):
        # logger
        self.log.info('handle_dont_understand_correctness')
        # spiegazione di quello che sta accadendo
        self.speak('Mi hai chiesto di imparare un nome per te')
        self.speak('Io ho capito che vuoi che io ti chiami: {}'.format(self.info['name']))
        self.speak('Ho capito bene? Ti posso chiamare {} ? '.format(self.info['name']), expect_response = True, wait=True)

    ''' Per l'esecuzione di questo intent e necessario che l'utente pronunci una parola indicata nel file 'Stop.voc'.
        Questo intent si occupa di gestire la cancellazione dell'operazione da parte dell'utente.
        Questo intent si attiva nel momento in cui in qualsiasi momento l'utente risponde con eg. 'stop'. '''
    @intent_handler(IntentBuilder('Stop').require('Stop'))
    def handle_stop(self, message):
        # logger
        self.log.info('handle_stop')
        # spiegazione di quello che sta accadendo
        self.speak('Va bene, operazione annullata')
        
        # reimpostsa il valore al valore origianale
        self.info['name'] = self.config_core['user_name']
        # risposta se un nome era gia presente un nome per l'utente 
        if self.is_setUpAlreadyAName:
            # conferma del non avvenuto cambiamento
            self.speak_dialog("dont.change.my.name", self.info)
        # risposta se non era presente un nome per l'utente
        else:
            self.sepak('Va bene, imparerò il tuo nome la prossima volta')
        # resetto i flag 
        self.re_set()
        
    def is_setUpAlreadyAName(self):
        return  (self.config_core['user_name'] != None and self.config_core['user_name'] != "" and self.config_core['user_name'] != '')
     

    def re_set(self):
        self.retry = False
        self.reset = False

        


def create_skill():
    return SetMyNameSkill()
