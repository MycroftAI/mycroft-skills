from test.integrationtests.skills.skill_tester import SkillTest


def test_runner(skill, example, emitter, loader):
    return SkillTest(skill, example, emitter).run(loader)