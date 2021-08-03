# Run skill changes against the last major release of Mycroft Core but install
# the latest version of all skills.
ARG major_release
FROM voight-kampff-mark-1:${major_release} as config_builder
ARG pull_request
ARG platform
ARG branch_name
ARG repo_url
ARG github_user
ARG github_api_key
ENV GITHUB_API_KEY=$github_api_key
RUN msm update
# Remove mycroft-stock skill. TODO: Remove in 21.08
RUN grep --invert-match mycroft-stock default.yml | tee /tmp/default.yml && mv /tmp/default.yml default.yml
# Load updated test cases for default skills...
# The test_setup.py script was previously executed in the voight-kampff-mark-1 image.
# Any changes to the naming of feature files will result in both the old and new
# feature files being executed in the test run.  The short term fix for this is
# to remove the feature files from the voight-kampff-mark-1 image before the
# test_setup.py script is run again.  The long-term fix is to move the execution of
# test_setup.py to inside run_test_suite.sh and to add a cleanup step after the tests complete.
RUN rm /opt/mycroft/mycroft-core/test/integrationtests/voight_kampff/features/*.feature
RUN python -m test.integrationtests.voight_kampff.test_setup \
    --config default.yml \
    --platform $platform \
    --branch $branch_name \
    --repo-url $repo_url
WORKDIR /opt/mycroft/mycroft-core
COPY test-requirements.txt skill-test-requirements.txt
RUN .venv/bin/python -m pip install -r skill-test-requirements.txt
COPY build_test_config.py .
COPY .gitmodules .
RUN .venv/bin/python build_test_config.py --pull-request $pull_request --platform $platform

# Use multi-stage build to forget the GitHub credentials from the previous stage
FROM config_builder as test_setup
ARG platform
ARG branch_name
ARG repo_url
# Load test cases for skill to test
RUN python -m test.integrationtests.voight_kampff.test_setup \
    --config test_skill.yml \
    --platform $platform \
    --branch $branch_name \
    --repo-url $repo_url
# Set working directory for testing
WORKDIR /opt/mycroft/mycroft-core/test/integrationtests/voight_kampff
