# """
# File_Name: test_system_methods.py
# Desc: This file contains the step definitons for the system.py methods
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 09/14/2020
# __modified__ = "Sharmila Vairamani" status code change due to bug fix - 09/17/2020

# """

# import time
# from pytest_bdd import scenarios, given, when, then, parsers
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from Kiosk.tests.Apis.Responses.system_info_response import SystemInfoResponse
# from webframework.kiosk.common.Constants.Api.system import SystemStates, SystemStatesTransitionTime, SystemErrorCodes
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder

# scenarios('../../features/system.feature')
# logger = Logger("test_system_methods")


# def invoke_base_api(url, api_name):
#     """
#     This function is used to validate all the request which returns common response such as message is "ok" and
#     error code as 0
#     @param url: The endpoints of the request
#     @param api_name: The name of the api that has been requested
#     """
#     payload = ""
#     api_request = ApiRequest(url=url, request_type=ApiRequestType.Put)
#     response = api_request.submit()
#     logger.info(f"response from the uv lamp {api_name} =>{response}")
#     assert (response.message, response.error_code) == ("ok", 0), \
#         f"Failed to {api_name} message {response.message} error_code {response.error_code}"


# @when('Request system to start')
# @then('Request system to start')
# def request_system_start_up():
#     url = UrlBuilder().get_api_url("system_start_up_url")
#     api_name = "start_up"
#     invoke_base_api(url, api_name)


# @when('Request system to shutdown')
# def system_shut_down():
#     url = UrlBuilder().get_api_url("system_shut_down_url")
#     api_name = "system_shut_down"
#     invoke_base_api(url, api_name)


# @when('Request system to wake up')
# @then('Request system to wake up')
# def request_system_wake_up():
#     url = UrlBuilder().get_api_url("system_wake_up_url")
#     api_name = "wake_up"
#     invoke_base_api(url, api_name)


# @when('Request system to sleep')
# def system_sleep():
#     url = UrlBuilder().get_api_url("system_sleep_url")
#     api_name = "system_sleep"
#     invoke_base_api(url, api_name)


# @when('Request system to reset')
# def system_reset():
#     url = UrlBuilder().get_api_url("system_reset_url")
#     api_name = "system_reset"
#     invoke_base_api(url, api_name)


# @then(parsers.parse(
#     'Validate system transition state from {transition_state} to {end_state} for the duration {duration}'))
# @when(parsers.parse(
#     'Validate system transition state from {transition_state} to {end_state} for the duration {duration}'))
# def validate_system_info(transition_state, end_state, duration):
#     logger.info(f"Entering validate system info")
#     duration = int(duration)
#     expected_system_state = end_state
#     url = UrlBuilder().get_api_url("system_info_url")
#     prime_solvent_info_request = ApiRequest(url=url, request_type=ApiRequestType.Get,
#                                             response_type=SystemInfoResponse)
#     start_time = time.time()
#     while time.time() - start_time < duration:
#         system_info_response = prime_solvent_info_request.submit()
#         system_state = system_info_response.data[4].get('value')
#         if system_state == end_state:
#             break
#         else:
#             assert system_state == transition_state, f"The state of the system is ==>{system_state}"
#         time.sleep(1)
#     assert system_state == expected_system_state, f" Failed to reach steady state"
#     logger.info("* *********************** The test ends for the system*******************")


# @given('Initial setup of the system')
# def set_up():
#     logger.info("The test for system starts")
#     logger.info("Initial setup of the system")
#     url = UrlBuilder().get_api_url("system_info_url")
#     prime_solvent_info_request = ApiRequest(url=url, request_type=ApiRequestType.Get,
#                                             response_type=SystemInfoResponse)
#     system_info_response = prime_solvent_info_request.submit()
#     system_state = system_info_response.data[4].get('value')

#     if system_state == SystemStates.asleep:
#         request_system_wake_up()
#         validate_system_info(SystemStates.busy, SystemStates.ready, SystemStatesTransitionTime.max_waking_up_time)

#     elif system_state == SystemStates.uninitialized:
#         request_system_start_up()
#         validate_system_info(SystemStates.initializing, SystemStates.ready,
#                              SystemStatesTransitionTime.max_initializing_time)
#     else:
#         logger.info("The state of the system is Ready")


# @then(parsers.parse('Validate system throws an error when system is made to {reset} with request {request_url}'))
# def call_rotary_tray_move(request_url):
#     url = UrlBuilder().get_api_url(request_url)
#     payload = ""
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     assert response.error_code == SystemErrorCodes.error, f" The actual error code {response.error_code}"
#     logger.info("* *********************** The test ends for the system*******************")

