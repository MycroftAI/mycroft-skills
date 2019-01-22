# How to contribute

This repository is a little different than most you'll find on Github.  It consists of primarily submodule links to Skills which actually live in other Github repositories.  Due to the complication of submodules, most will never use `git` commands directly against this repository.

Instead, the [Mycroft Skill Kit](https://mycroft.ai/documentation/skills/msk) is the preferred mechanism for submitting
and updating Skills to this repository.  Submitted skills are reviewed by a team of Mycroft community members to ensure quality and that community standards are followed. You can [read more here about our Skills Acceptance Process](https://mycroft.ai/documentation/skills/skills-acceptance-process/). 

Once a Skill is approved and merged, it will become a submodule here and will appear in the [Mycroft Marketplace](https://market.mycroft.ai).


## What is the Mycroft Skill Kit?

The Mycroft Skill Kit, is a Python utility we created that hides the complications of creating and updating submodules in this repo.  It is possible to submit Skills manually, but it is tricky and error-prone so not recommended.

MSK is installed automatically with any Mycroft installation.  You generally can access it using the ```mycroft-msk``` alias.  You can also examine the code directly from the [MSK repo](https://github.com/mycroftai/mycroft-skills-kit).


## Before using MSK to submit your Skill to Mycroft

Skills in this repo should be ready for others to use, not just experiments.

This means you should have done all of these things:
* Created a README.md that conforms to the standard format.  Use the [Skill Meta Editor](https://raw.githack.com/MycroftAI/mycroft-skills/18.08/meta_editor.html)
  to easily create it.
* Added whatever license you want to release your Skill under
* Implemented basic Skill [autotests](https://mycroft.ai/documentation/skills/automatic-testing/).
* Committed all your code to Github.


## Using MSK to submit a new Skill or update an existing Skill

Once your Skill is ready for the Marketplace, submitting it for review is as
easy as:
```
cd <local-path-to-your-skill>
mycroft-msk submit .
```
or:
```
mycroft-msk submit <local-path-to-your-skill>
```

That's it!  The currently active branch of your repo will be submitted.  If a PR is
already pending approval, that PR will be updated in place.

By policy, changes to a README.md or translations will automatically be approved and
merged.  New skills or new functionality will be re-reviewed before approval and merging.

__Note:__ If you have two-factor authentication enabled for github, you will need to generate a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) and use the `-t` flag. E.g.

    mycroft-msk -t submit <local-path-to-your-skill>

# Links to Additional Resources

* [Mycroft Skill API documentation](https://mycroft-core.readthedocs.io/en/master/)
* [Help developing skills](https://chat.mycroft.ai/community/channels/skills)
* [MSK repo](https://github.com/mycroftai/mycroft-skills-kit)
* [Skill Feedback channel on the Forum](https://community.mycroft.ai/c/skill-feedback) 
