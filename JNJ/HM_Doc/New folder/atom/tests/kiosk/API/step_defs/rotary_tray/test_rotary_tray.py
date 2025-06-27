# """
# File_Name: test_rotary_tray.py
# Desc: This file contains the step definitons for the rotary tray tests
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 03/09/2020
# --modified-- = "Sharmila Vairamani" changed the logger implementation- 04/21/2020

# """
# import time
# from pytest_bdd import when, then, given
# from pytest_bdd import scenarios
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from Kiosk.tests.Apis.Responses.RotaryTrayResponse.rotary_tray_configuration_response import RotaryTrayConfigurationResponse
# from Kiosk.tests.Apis.Responses.RotaryTrayResponse.rotary_tray_info_response import RotaryTrayInfoResponse
# from Kiosk.tests.Apis.Request.RotaryTrayRequest.rotary_tray_move_request import RotaryTrayMoveRequest
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder


# logger = Logger("test_rotary_tray")
# scenarios('../../../features/rotary_tray.feature')


# @given('Initial setup of the rotary tray')
# def set_up():
#     rotary_tray_info_response = invoke_rotary_info()
#     if rotary_tray_info_response.state == "EXTENDED":
#         call_rotary_tray_retract()
#     time.sleep(1)  # TODO verify how instrument/API behaves when integrated with actual isym
#     logger.info(
#         '\n************************** The test starts for the rotary tray ******************')
#     url = UrlBuilder().get_api_url("rotary_tray_home_url")
#     invoke_base_api(url, 'rotary_tray_home', '')
#     rotary_tray_info_response = invoke_rotary_info(True, 20)
#     logger.info("******This is to debug******************************")
#     logger.info(f"rotary tray home response => {rotary_tray_info_response}")


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


# def invoke_rotary_info(check_for_loaded=False, number_of_seconds_to_wait=10) -> RotaryTrayInfoResponse:
#     """
#         This function creates request for the info api and returns the response
#         :param check_for_loaded:
#         :param secs:
#         :return: RotaryTrayInfoResponse

#         """
#     url = UrlBuilder().get_api_url("rotary_tray_info_url")
#     payload = ""
#     request = ApiRequest(url=url, request_type=ApiRequestType.Get, response_type=RotaryTrayInfoResponse)
#     rotary_tray_info_response = request.submit()
#     if check_for_loaded:
#         count = 0
#         while count < number_of_seconds_to_wait:
#             if (rotary_tray_info_response.state == "LOADED") or (rotary_tray_info_response.state == "EXTENDED"):
#                 break
#             time.sleep(1)
#             rotary_tray_info_response = request.submit()
#             count = count + 1
#         assert rotary_tray_info_response.state == "LOADED" or "EXTENDED", f"failed to load rotary tray ," \
#                                                                           f" state => {rotary_tray_info_response.state}"
#     return rotary_tray_info_response


# @when('Request rotary tray to extend')
# def call_rotary_tray_extend():
#     url = UrlBuilder().get_api_url("rotary_tray_extend_plate_url")
#     payload = ""
#     api_name = "rotary_tray_extend"
#     invoke_base_api(url, api_name, payload)


# @then('Validate rotary tray state: <expected_state> active_plate: <expected_active_plate> angle: <expected_angle> '
#       'error_code: <expected_error_code>')
# def call_rotary_tray_info(expected_state, expected_active_plate, expected_angle, expected_error_code):
#     expected_state = str(expected_state)
#     expected_angle = int(expected_angle)
#     expected_active_plate = int(expected_active_plate)
#     expected_error_code = int(expected_error_code)
#     rotary_tray_info_response = invoke_rotary_info(True, 20)
#     assert rotary_tray_info_response.state == expected_state, f"Failed to load, state = {rotary_tray_info_response.state}"
#     assert rotary_tray_info_response.angle == expected_angle, f"Failed to reach the angle = {rotary_tray_info_response.angle}"
#     assert rotary_tray_info_response.active_plate == expected_active_plate, f"Failed to reach the active_plate = {rotary_tray_info_response.active_plate} "
#     assert rotary_tray_info_response.error_code == expected_error_code, f"Failed to reach ok status = {rotary_tray_info_response.error_code}"
#     logger.info('\n*********************The test ends for the rotary tray*************************************')


# @when('Request the rotary tray to retract')
# def call_rotary_tray_retract():
#     url = UrlBuilder().get_api_url("rotary_tray_retract_plate_url")
#     payload = ""
#     api_name = "rotary_tray_retract"
#     invoke_base_api(url, api_name, payload)


# @then('Validate that the api should throw an error when the rotary tray move')
# def call_rotary_tray_move():
#     url = UrlBuilder().get_api_url("rotary_tray_move_url")
#     move_request = RotaryTrayMoveRequest("PLATE_NUMBER", 1)
#     payload = move_request.to_json_string()
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     logger.debug(response)
#     assert (response.message, response.error_code) == ("cannot perform when plate is not retracted.", 5003), \
#         "Failed to {} message {} error_code {}".format(
#             response.message, response.error_code)
#     logger.info('\n*********************The test ends for the rotary tray*************************************')


# @then('Request the rotary tray to retract')
# def call_rotary_tray_retract():
#     url = UrlBuilder().get_api_url("rotary_tray_retract_plate_url")
#     payload = ""
#     api_name = "rotary_tray_retract"
#     invoke_base_api(url, api_name, payload)


# @then('validate the system throws an error when we extent the extended rotary tray')
# def validate_rotary_tray_error():
#     url = UrlBuilder().get_api_url("rotary_tray_extend_plate_url")
#     payload = ""
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     rotary_tray_response = api_request.submit()
#     logger.debug('rotary_tray_configuration_response => ', rotary_tray_response.message)
#     assert (rotary_tray_response.message, rotary_tray_response.error_code) == ("Command rejected because state is "
#                                                                                "EXTENDED instead of LOADED", 5005), \
#         "Failed to message {} error_code {}".format(

#             rotary_tray_response.message, rotary_tray_response.error_code)
#     logger.info('\n*********************The test ends for the rotary tray*************************************')


# @then('validate the system throws an error when we retract the rotary tray')
# def validate_rotary_tray_error():
#     url = UrlBuilder().get_api_url("rotary_tray_retract_plate_url")
#     payload = ""
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     rotary_tray_response = api_request.submit()
#     logger.debug(f"rotary_tray_configuration_response => {rotary_tray_response.message}")
#     assert (rotary_tray_response.message, rotary_tray_response.error_code) == (
#         "Command rejected because state is LOADED instead of EXTENDED",
#         5005), "Failed to message {} error_code {}".format(

#         rotary_tray_response.message, rotary_tray_response.error_code)
#     logger.info('\n*********************The test ends for the rotary tray*************************************')


# @when('Request rotary tray to move plate <plate_position>')
# def call_rotary_tray_move(plate_position):
#     url = UrlBuilder().get_api_url("rotary_tray_move_url")
#     move_request = RotaryTrayMoveRequest("PLATE_NUMBER", int(plate_position))

#     payload = move_request.to_json_string()
#     api_name = "rotary_tray_move"
#     invoke_base_api(url, api_name, payload)


# @when('Request rotary tray configuration')
# def call_rotary_tray_configuration():
#     url = UrlBuilder().get_api_url("rotary_tray_configuration_url")
#     payload = ""
#     request = ApiRequest(url=url, request_type=ApiRequestType.Get, response_type=RotaryTrayConfigurationResponse)
#     rotary_tray_response = request.submit()
#     logger.debug('rotary_tray_configuration_response => ', rotary_tray_response)
#     assert (0, "ok", 3) == (rotary_tray_response.error_code, rotary_tray_response.message,
#                             rotary_tray_response.no_of_plates)


# @when('Request rotary tray to home')
# def call_rotary_tray_home():
#     url = UrlBuilder().get_api_url("rotary_tray_home_url")
#     payload = ""
#     api_name = "rotary_tray_home"
#     invoke_base_api(url, api_name, payload)


# @when('Request rotary tray to move plate <move_mode>')
# def call_rotary_tray_move(move_mode):
#     url = UrlBuilder().get_api_url("rotary_tray_move_url")
#     move_request = RotaryTrayMoveRequest(str(move_mode), 0)
#     payload = move_request.to_json_string()
#     api_name = "rotary_tray_move"
#     invoke_base_api(url, api_name, payload)
