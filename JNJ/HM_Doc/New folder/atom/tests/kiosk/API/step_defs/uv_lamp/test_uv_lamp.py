# """
# File_Name: test_uv_lamp.py
# Desc: This file contains the step definitons for the uv lamp tests
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 03/09/2020
# --modified-- = "Sharmila Vairamani" changed the logger implementation- 04/21/2020

# """

# import time
# from pytest_bdd import scenarios, given, when, then
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from Kiosk.tests.Apis.Responses.LampResponse.lamp_info_response import LampInfoResponse
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder

# scenarios('../../../features/uv_lamp.feature')
# logger = Logger("test_uv_lamp")


# def invoke_base_api(url, api_name):
#     payload = ""
#     api_request = ApiRequest(url=url, request_type=ApiRequestType.Put)
#     response = api_request.submit()
#     logger.info(f"response from the uv lamp {api_name} =>{response}")
#     assert (response.message, response.error_code) == ("ok", 0), \
#         f"Failed to {api_name} message {response.message} error_code {response.error_code}"


# @given('Initial setup of the uv lamp')
# def initial_set_up():
#     url = UrlBuilder().get_api_url("lamp_clear_alarm_url")
#     api_name = "clear_alarm"
#     invoke_base_api(url, api_name)
#     logger.info('\n*********************The test starts for the uv lamp*************************************')


# @when('Request uv lamp power on')
# def call_uv_lamp_on():
#     url = UrlBuilder().get_api_url("lamp_power_on_url")
#     api_name = "power_on"
#     invoke_base_api(url, api_name)


# @then(
#     'Validate uv lamp new state: <expected_new_state> old state: <expected_old_state>  last_error_code: <expected_last_error_code>')
# def call_lamp_info(expected_new_state, expected_old_state, expected_last_error_code):
#     max_time_lamp_to_turn_on = 10
#     expected_new_state = str(expected_new_state)
#     expected_old_state = str(expected_old_state)
#     expected_last_error_code = int(expected_last_error_code)
#     lamp_info_response, url = request_lamp_info()
#     lamp_info_response = get_lamp_state(lamp_info_response, max_time_lamp_to_turn_on, url)
#     assert lamp_info_response.new_state == expected_new_state, f"Failed to load, state = {lamp_info_response.new_state}"
#     assert lamp_info_response.old_state == expected_old_state, f"Failed to reach the angle = {lamp_info_response.old_state}"
#     assert lamp_info_response.last_error_code == expected_last_error_code, f"Failed to reach the active_plate = {lamp_info_response.last_error_code}"
#     logger.info(lamp_info_response.total_on_time_ms)

#     logger.info('\n*********************The test ends for the uv lamp*************************************')


# @when('Request uv lamp power off')
# def call_uv_lamp_off():
#     url = UrlBuilder().get_api_url("lamp_power_off_url")
#     api_name = "lamp_off"
#     invoke_base_api(url, api_name)


# @when('Request uv lamp clear alarm')
# def call_uv_lamp_clear_alarm():
#     url = UrlBuilder().get_api_url("lamp_clear_alarm_url")
#     api_name = "clear_alarm"
#     invoke_base_api(url, api_name)


# @when('Trigger an error on the uv lamp')
# def call_trigger_error():
#     url = UrlBuilder().get_api_url("lamp_trigger_error_url")
#     api_name = "trigger_error"
#     invoke_base_api(url, api_name)


# @then('Validate the last lamp on time is updated the moment the lamp is turned on')
# def get_last_lamp_on_time_info():
#     expected_new_state, lamp_info_response, max_time_lamp_to_turn_on = validate_lamp_ready_state()
#     initial_last_lamp_on_time = lamp_info_response.last_lamp_on_time
#     logger.info(f"initial Last lamp on time = > {initial_last_lamp_on_time}")
#     call_uv_lamp_off()
#     call_uv_lamp_on()
#     lamp_info_response, url = request_lamp_info()
#     lamp_info_response = get_lamp_state(lamp_info_response, max_time_lamp_to_turn_on, url)
#     assert lamp_info_response.new_state == expected_new_state, f"Failed to load, state = {lamp_info_response.new_state}"
#     final_last_lamp_on_time = lamp_info_response.last_lamp_on_time
#     logger.info(f"final lamp last on time => {final_last_lamp_on_time} ")
#     assert final_last_lamp_on_time > initial_last_lamp_on_time, f" The last lamp on time is not updated"


# @then('Validate the total lamp on time is updated the moment the lamp is turned off')
# def get_total_lamp_on_time():
#     expected_new_state, lamp_info_response, max_time_lamp_to_turn_on = validate_lamp_ready_state()
#     initial_total_lamp_on_time_ms = lamp_info_response.total_on_time_ms
#     logger.info(f"Initial total lamp on time=> {initial_total_lamp_on_time_ms}")
#     call_uv_lamp_off()
#     lamp_info_response, url = request_lamp_info()
#     expected_new_state = "OFF"
#     assert lamp_info_response.new_state == expected_new_state, f"Failed to load, state = {lamp_info_response.new_state}"
#     final_total_lamp_on_time_ms = lamp_info_response.total_on_time_ms
#     logger.info(f"Final total lamp on time=> {final_total_lamp_on_time_ms}")
#     assert final_total_lamp_on_time_ms > initial_total_lamp_on_time_ms, f" Failed to update the total lamp on time"


# def request_lamp_info():
#     """
#     This function returns the url for sending th info request and also the response object of the info request
#     :return: lamp_info_response, url
#     """
#     url = UrlBuilder().get_api_url("lamp_info_url")
#     logger.debug(f"lamp_info url => {url}")
#     payload = ""
#     api_request = ApiRequest(url=url, request_type=ApiRequestType.Get, response_type=LampInfoResponse)
#     lamp_info_response = api_request.submit()
#     return lamp_info_response, url


# def get_lamp_state(lamp_info_response, max_time_lamp_to_turn_on, url):
#     """
#     This function returns the response after the lamp reached the desired state
#     :param lamp_info_response:
#     :param max_time_lamp_to_turn_on:
#     :param url:
#     :return: lamp_info_response
#     """
#     start_time = time.time()
#     while time.time() - start_time < max_time_lamp_to_turn_on:
#         if lamp_info_response.new_state == "READY" or lamp_info_response.new_state == "OFF" or lamp_info_response.new_state == "ERROR":
#             break
#         api_request = ApiRequest(url=url, request_type=ApiRequestType.Get, response_type=LampInfoResponse)
#         lamp_info_response = api_request.submit()
#         time.sleep(1)
#     return lamp_info_response


# def validate_lamp_ready_state():
#     """
#     This function validates the state of the lamp is ready and returns the response
#     :return: expected_new_state, lamp_info_response, max_time_lamp_to_turn_on
#     """
#     max_time_lamp_to_turn_on = 10
#     expected_new_state = "READY"
#     lamp_info_response, url = request_lamp_info()
#     lamp_info_response = get_lamp_state(lamp_info_response, max_time_lamp_to_turn_on, url)
#     assert lamp_info_response.new_state == expected_new_state, f"Failed to load, state = {lamp_info_response.new_state}"
#     return expected_new_state, lamp_info_response, max_time_lamp_to_turn_on






