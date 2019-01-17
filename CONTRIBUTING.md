# How to contribute

This repository is a little different than most you'll find on Github.  It consists of
primarily submodule links to skills which actually live in other Github repositories.  Due
to the complication of submodules, most will never use git commands directly
against this repository.

Instead, the Mycroft Skill Kit is the preferred mechanism for submitting
and updating skills to this repository.  Submitted skills are reviewed by a
team of Mycroft community members to ensure quality and that community standards
are followed.

Once a skill is approved and merged, it will become a submodule here and will
appear in the [Mycroft Marketplace](https://market.mycroft.ai).


## What is the Mycroft Skill Kit?

The Mycroft Skill Kit, is a Python utility we created that hides the
complications of creating and updating submodules in this repo.  It is possible
to submit skills manually, but it is tricky and error-prone so not recommended.

MSK is installed automatically with any Mycroft installation.  You generally can
access it using the ```mycroft-msk``` alias.  You can also examine the code
directly from the [MSK repo](https://github.com/mycroftai/mycroft-skills-kit).


## Before using MSK to submit your skill to Mycroft

Skills in this repo should be ready for others to use, not just experiments.
This means you should have done all of these things:
* Created a README.md that conforms to the standard format.  Use the [Skill Meta Editor](https://raw.githack.com/MycroftAI/mycroft-skills/18.08/meta_editor.html)
  to easily create it.
* Added whatever license you want to release your skill under.
* Implemented basic skill autotests.
* Committed all your code to Github.


## Using MSK to submit a new skill

Once your skill is ready for the Marketplace, submitting it for review is as
easy as:
```
mycroft-msk submit .
```

That's it!  The currently active branch of your repo will be submitted.


## Updating an existing skill

A skill that is already in the Marketplace can easily be updated with:
```
mycroft-msk update .
```

Changes to a README.md or translations will automatically be approved and
merged.  New functionality will be re-reviewed before approval and merging.


# Links to Additional Reources

* [Mycroft Skill API documentation](https://mycroft-core.readthedocs.io/en/master/)
* [Help developing skills](https://chat.mycroft.ai/community/channels/skills)
* [MSK repo](https://github.com/mycroftai/mycroft-skills-kit)

