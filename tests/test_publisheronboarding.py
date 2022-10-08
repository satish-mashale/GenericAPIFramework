from assertpy import assert_that, soft_assertions

from base.Base import logger
from controller.workflowfeatures.Publisheronboarding import Publisheronboarding
from utils.print_helpers import pretty_print

onboarding = Publisheronboarding()


def test_publisher_onboarding(request, test_data):
    # Get Test case name and make sure test data key is same as that of test case name
    testname = request.node.name
    logger.info(f"Started test execution for {testname}")
    res = onboarding.create_publisher(testname,'/inventorymgmt/onboard/publisher', test_data['workflow'][testname])
    logger.info(pretty_print(res.text))
    with soft_assertions():
        assert_that(res).is_not_none()
        #assert_that(res.json['lastName']).is_equal_to(test_data['workflow'][testname]['publisher']['lastName'])


def test_publisher_onboarding_for_ortbpubs(request, test_data):
    pass
