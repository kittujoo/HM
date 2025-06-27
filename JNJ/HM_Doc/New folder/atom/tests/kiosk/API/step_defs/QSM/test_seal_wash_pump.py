# """
# File_Name: test_seal_wash_pump.py
# Desc: This file contains the step definitons for the seal wash pump tests
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 07/09/2020


# """
# # This feature is not test complete as there are some contradictory on the requirements. These requirements needed to be
# #  reviewed by the HW/FW folks. The FTN PRD detail is not sufficient to determine full Orion behavior
# #  Therefore there is a hold off on further dev on Service and Test for this feature, at this point


# import time
# from pytest_bdd import scenarios, given, when, then
# from Kiosk.tests.Apis.Request.QSM.SealWashPump.start_prime_request import SealWashPumpStartPrimeRequest
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from Kiosk.tests.Apis.Responses.QSM.SealWashPump.seal_wash_pump_info_response import SealWashPumpInfoResponse
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder

# scenarios('../../../features/seal_wash_pump.feature')
# logger = Logger("test_seal_wash_pump")


# def invoke_base_api(url, api_name, payload):
#     """
#         This function creates request for the given url and asserts the returned response
#         :param url: The requested url
#         :param api_name: Name of the component's api
#         :param payload: Input parameter
#         :return: Void

#         """
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()

#     logger.info(f" {api_name} response => {response} ")
#     assert (response.message, response.error_code) == ("ok", 0), \
#         f"Failed to {api_name} message {response.message} error_code {response.error_code}"


# @given('Initial setup of the seal wash pump')
# def initial_set_up():
#     url = UrlBuilder().get_api_url("swp_prime_clear_alarm_url")
#     api_name = "clear_alarm"
#     payload = ""
#     invoke_base_api(url, api_name, payload)
#     logger.info('\n*********************The test starts for the uv lamp*************************************')


# @when('Request the seal wash pump to start priming for the given <duration>')
# def call_seal_wash_pump_prime_start(duration):
#     url = UrlBuilder().get_api_url("swp_prime_start_url")
#     api_name = "start"
#     start_request = SealWashPumpStartPrimeRequest(int(duration))
#     payload = start_request.to_json_string()
#     invoke_base_api(url, api_name, payload)


# @then('Validate seal wash pump info with <expected_state>,<expected_remaining_time_ms>,<expected_error_code> for the <duration>')
# def validate_prime_duration(expected_state, expected_remaining_time_ms, expected_error_code, duration):
#     duration = int(duration) + 1 # adding 1 sec to include simulator's time resolution of one sec
#     expected_remaining_time_ms = int(expected_remaining_time_ms)
#     expected_state = str(expected_state)
#     expected_error_code = int(expected_error_code)
#     seal_wash_pump_info_response = get_seal_wash_pump_state(duration)
#     assert seal_wash_pump_info_response.state == expected_state, f"Failed to  complete te priming, actual state => {seal_wash_pump_info_response.state} "
#     assert seal_wash_pump_info_response.remaining_time_ms == expected_remaining_time_ms, f"Failed to  complete the priming, actual state => {seal_wash_pump_info_response.state}"
#     assert seal_wash_pump_info_response.error_code == expected_error_code, f" actual error code => {seal_wash_pump_info_response.error_code}"


# def get_seal_wash_pump_state(max_time_to_prime):
#     """
#        This function returns the response after the seal wash pump reached the desired state
#        :param max_time_to_prime:
#        :return: lamp_info_response
#        """
#     start_time = time.time()
#     while time.time() - start_time < max_time_to_prime:
#         seal_wash_pump_info_response = request_seal_wash_pump_info()
#         if seal_wash_pump_info_response.state == "IDLE":
#             break

#         time.sleep(1)
#     return seal_wash_pump_info_response


# def request_seal_wash_pump_info():
#     """
#     This function returns the url for sending the info request and also the response object of the info request
#     :return: lamp_info_response, url
#     """
#     url = UrlBuilder().get_api_url("swp_info_url")
#     logger.debug(f"swp_info url => {url}")
#     api_request = ApiRequest(url=url, request_type=ApiRequestType.Get, response_type=SealWashPumpInfoResponse)
#     seal_wash_pump_info_response = api_request.submit()
#     return seal_wash_pump_info_response
