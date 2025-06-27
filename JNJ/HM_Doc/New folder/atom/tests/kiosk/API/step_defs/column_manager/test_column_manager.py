# """
# File_Name: test_column_manager.py
# Desc: This file contains the step definitons for the rotary tray tests
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 04/07/2020
# --modified-- = "Sharmila Vairamani" changed the logger implementation- 04/21/2020
# --modified-- = "Sharmila Vairamani" added clear alarm and trigger error test - 06/25/2020


# """
# import time
# from pytest_bdd import when, then, given
# from pytest_bdd import scenarios
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from Kiosk.tests.Apis.Request.ColumnManagerRequest.clear_alarm_request import ColumnManagerClearAlarmRequest
# from Kiosk.tests.Apis.Request.ColumnManagerRequest.control_request import ColumnManagerControlRequest
# from Kiosk.tests.Apis.Request.ColumnManagerRequest.set_point_request import ColumnManagerSetPointRequest
# from Kiosk.tests.Apis.Request.ColumnManagerRequest.trigger_error_request import ColumnManagerTriggerAlarm
# from Kiosk.tests.Apis.Responses.ColumnManagerResponse.column_manager_info_response import ColumnManagerInfoResponse, \
#     ColumnInfo
# from webframework.kiosk.common.Constants.Api.column_manager import ColumnManagerErrorMessages, ColumnManagerErrorCodes, \
#     ColumnManagerConstants, ColumnManagerStates
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder

# scenarios('../../../features/column_manager.feature')

# logger = Logger("test_column_manager")

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
#     logger.info(f" {api_name} response  => {response}")
#     assert (response.message, response.error_code) == ("ok", 0), \
#         f"Failed to {api_name} message {response.message} error_code {response.error_code}"


# @given('Initial setup of the column manager')
# def set_up():
#     logger.info(" ************The test starts for the column manager ******************")
#     initial_temperature = ColumnManagerConstants.temperature
#     action = "ON"
#     logger.info(f"Setting up initial temperatures {initial_temperature} for the ColumnManager ")
#     initial_column_set_up("CM1-Col1", initial_temperature, action)
#     initial_column_set_up("CM1-Col2", initial_temperature, action)
#     initial_column_set_up("CM1-Col3", initial_temperature, action)
#     logger.info("****The set up  for the column is done *******************************")


# def initial_column_set_up(column_id, initial_temperature, action):
#     """
#     This function is the preliminary setup for the column manager to execute various test on the columns. Here any error
#     condition is cleared of all the column and the control is turned on and the temperature of all the columns is set to a desired temperature
#     @param column_id:
#     @param initial_temperature:
#     @param action:
#     @return:

#     """
#     clear_column_alarm(column_id)

#     set_column_control(action, column_id)

#     set_column_temperature(column_id, initial_temperature)

#     validate_initial_column_set_up(column_id)


# def set_column_temperature(column_id, initial_temperature):
#     """
#     This function sets the temperature for the given column
#     :param column_id:
#     :param initial_temperature:
#     :return:
#     """
#     url = UrlBuilder().get_api_url("column_manager_setpoint_url")
#     set_point__request = ColumnManagerSetPointRequest(column_id, initial_temperature)
#     payload = set_point__request.to_json_string()
#     invoke_base_api(url, 'column_manager_control_url', payload)


# def set_column_control(action, column_id):
#     """
#     This function sets the control for the given column
#     :param action:
#     :param column_id:
#     :return:
#     """
#     url = UrlBuilder().get_api_url("column_manager_control_url")
#     control_request = ColumnManagerControlRequest(column_id, action)
#     payload = control_request.to_json_string()
#     invoke_base_api(url, 'column_manager_control_url', payload)


# def clear_column_alarm(column_id):
#     """
#     This function clear any error condition for the given column
#     :param column_id:
#     :return:
#     """
#     url = UrlBuilder().get_api_url("column_manager_clear_alarm_url")
#     clear_alarm_request = ColumnManagerClearAlarmRequest(column_id)
#     payload = clear_alarm_request.to_json_string()
#     invoke_base_api(url, 'column_manager_clear_alarm', payload)


# def validate_initial_column_set_up(column_id):
#     """
#     This function is to check for the temperature is set for the desired set point
#     @param column_id:
#     @return: void
#     """

#     logger.info("Starting to check the Target Temperature")

#     count = 0
#     target_reached = False
#     number_of_seconds_to_wait = ColumnManagerConstants.MaxTimeToReachMaxTemperature

#     while count < number_of_seconds_to_wait:
#         response_column_info_list = invoke_column_info().column_list
#         target_reached = has_target_reached(column_id, response_column_info_list)

#         if target_reached:
#             break
#         time.sleep(2)
#         count = count + 2

#     assert target_reached, f"Initial setup failed for column id =>{column_id}"


# @when('Request the control action to <action> for the column <column_id>')
# def call_column_manager_control_off(column_id, action):
#     url = UrlBuilder().get_api_url("column_manager_control_url")
#     control_request = ColumnManagerControlRequest(column_id, action)
#     payload = control_request.to_json_string()
#     invoke_base_api(url, 'column_manager_control_url', payload)


# @when('Set the desired <temperature> for the column <column_id>')
# def call_column_manager_set_point(temperature, column_id):
#     url = UrlBuilder().get_api_url("column_manager_setpoint_url")
#     set_point__request = ColumnManagerSetPointRequest(column_id, temperature)
#     payload = set_point__request.to_json_string()
#     invoke_base_api(url, 'column_manager_control_url', payload)


# @then(
#     'Validate the column <column_id> info for <action> for change in value of <state> <set_point> <target_temperature>')
# def call_column_manager_info(action, column_id, state, set_point, target_temperature):
#     number_of_seconds_to_wait = ColumnManagerConstants.MaxTimeToReachMaxTemperature
#     set_point = int(set_point)
#     target_temperature = int(target_temperature)
#     time.sleep(1)  # This needs to be removed once it is integrated with UI
#     validate_initial_column_information(action, column_id, target_temperature)

#     response_column_info_list = extract_target_column_information(column_id, number_of_seconds_to_wait)

#     validate_final_column_information(action, column_id, response_column_info_list, set_point, state,
#                                       target_temperature)
#     logger.info(" ************The  test ends for the column manager ******************")


# @then('Validate the <column_id> info change in <state> <set_point> <target_temperature>')
# def call_column_manager_info(action, column_id, state, set_point, target_temperature):
#     number_of_seconds_to_wait = ColumnManagerConstants.MaxTimeToReachMaxTemperature
#     set_point = int(set_point)
#     target_temperature = int(target_temperature)
#     time.sleep(1)  # This needs to be removed once it is integrated with UI
#     validate_initial_column_information_after_action_on(action, column_id, target_temperature)
#     response_column_info_list = extract_target_column_information(column_id, number_of_seconds_to_wait)
#     validate_final_column_information(action, column_id, response_column_info_list, set_point, state,
#                                       target_temperature)
#     logger.info(" ************The  test ends for the column manager ******************")



# @then('Validate the system throws an error for setting an <invalid_temperature> for column <column_id>')
# def validate_rotary_error(invalid_temperature, column_id):
#     url = UrlBuilder().get_api_url("column_manager_setpoint_url")
#     control_request = ColumnManagerSetPointRequest(column_id, invalid_temperature)
#     payload = control_request.to_json_string()
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     assert (response.message, response.error_code) == (
#         ColumnManagerErrorMessages.OutOfRangeMessage, ColumnManagerErrorCodes.OutOfRange), \
#         "Failed to {} message {} error_code {}".format(
#             response.message, response.error_code)
#     logger.info(" ************The  test ends for the column manager ******************")


# @when('Trigger an error on the column manager <column_id>')
# def trigger_error(column_id):
#     url = UrlBuilder().get_api_url("column_manager_trigger_error_url")
#     trigger_error_request = ColumnManagerTriggerAlarm(column_id)
#     payload = trigger_error_request.to_json_string()
#     invoke_base_api(url, 'column_manager_trigger_error_url', payload)


# @then('Validate the user cannot set the <temperature> for the column <column_id>')
# def validate_error(temperature, column_id):
#     url = UrlBuilder().get_api_url("column_manager_setpoint_url")
#     control_request = ColumnManagerSetPointRequest(column_id, temperature)
#     payload = control_request.to_json_string()
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     assert (response.message, response.error_code) == (
#         ColumnManagerErrorMessages.CommandRejectedInAlarmMessage, ColumnManagerErrorCodes.CommandRejectedInAlarm), \
#         "Failed to {} message {} error_code {}".format(
#             response.message, response.error_code)
#     logger.info(" ************The  test ends for the column manager ******************")


# @when('Request the clear alarm to clear the alarm condition for column <column_id>')
# def call_clear_alarm_request(column_id):
#     logger.info(" ************The  test starts for the column manager ******************")
#     url = UrlBuilder().get_api_url("column_manager_clear_alarm_url")
#     clear_alarm_request = ColumnManagerClearAlarmRequest(column_id)
#     payload = clear_alarm_request.to_json_string()
#     invoke_base_api(url, 'column_manager_clear_alarm', payload)


# @then('Validate the user cannot turn <action> the control for the column manager <column_id>')
# def validate_error(column_id, action):
#     url = UrlBuilder().get_api_url("column_manager_control_url")
#     control_request = ColumnManagerControlRequest(column_id, action)
#     payload = control_request.to_json_string()
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     assert (response.message, response.error_code) == (
#         ColumnManagerErrorMessages.CommandRejectedInAlarmMessage, ColumnManagerErrorCodes.CommandRejectedInAlarm), \
#         "Failed to {} message {} error_code {}".format(
#             response.message, response.error_code)
#     logger.info(" ************The  test ends for the column manager ******************")


# def extract_target_column_information(column_id, number_of_seconds_to_wait):
#     """
#     This function returns the column info response once the target state is reached
#     @param column_id:
#     @param number_of_seconds_to_wait:
#     @param set_point:
#     @param state:
#     @return:
#     """

#     count = 0
#     target_reached = False
#     while count < number_of_seconds_to_wait:
#         column_manager_info = invoke_column_info()
#         logger.info(f"ColumnManagerInfo Response  => {column_manager_info}")
#         response_column_info_list = column_manager_info.column_list

#         target_reached = has_target_reached(column_id, response_column_info_list)
#         if target_reached:
#             break

#         time.sleep(3)
#         count = count + 3
#     return response_column_info_list


# def validate_initial_column_information(action, column_id, target_temperature):
#     """
#     This function checks for cooling or heating state depending upon the current temperature when control is OFF
#     @param action:
#     @param column_id:
#     @param target_temperature:
#     @return:
#     """

#     column_manager_info = invoke_column_info()
#     response_column_info_list = column_manager_info.column_list
#     for response_column_info in response_column_info_list:

#         if response_column_info.resource_id == column_id and response_column_info.action == "OFF":
#             current_temperature = response_column_info.current_temperature
#             if current_temperature <= target_temperature:
#                 assert response_column_info.state == ColumnManagerStates.Idle

#                 logger.info(" **********************Column Current State: Idle****************")
#             else:
#                 assert response_column_info.state == ColumnManagerStates.Idle
#                 logger.info(" **********************Column Current State: idle ****************")



# def has_target_reached(column_id, response_column_info_list):
#     """
#     This function is to validate that the state of the column reached to the set temperature
#     @param column_id:
#     @param response_column_info_list:
#     @return: Boolean
#     """
#     target_reached = False
#     column_information = extract_column_information(column_id, response_column_info_list)
#     if column_information is not None and column_information.state == ColumnManagerStates.AtTarget:
#         target_reached = True

#     return target_reached


# def validate_final_column_information(action, column_id, response_column_info_list, set_point, state,
#                                       target_temperature):
#     """
#     This function validate the final info response with the actual info response
#     @param action:
#     @param column_id:
#     @param response_column_info_list:
#     @param set_point:
#     @param state:
#     @param target_temperature:
#     @return:
#     """
#     actual_column_information = extract_column_information(column_id, response_column_info_list)

#     expected_column_information = build_column_information(action, column_id, set_point, state,
#                                                            target_temperature)
#     logger.debug(f"actual column information => {actual_column_information}")
#     logger.debug(f"expected column information => {expected_column_information}")
#     validate_column_information(actual_column_information, expected_column_information)


# def validate_column_information(actual_column_information, expected_column_information):
#     """
#     This function checks the actual response from the response api with the expected response from the feature file
#     @param actual_column_information:
#     @param expected_column_information:
#     @return:
#     """
#     assert actual_column_information.resource_id == expected_column_information.resource_id, f"failed to set the column id {actual_column_information.resource_id}"
#     assert actual_column_information.action == expected_column_information.action, f"failed to control action {actual_column_information.action}"
#     assert actual_column_information.set_point == expected_column_information.set_point, f"failed to set the set point {actual_column_information.set_point}"
#     assert actual_column_information.state == expected_column_information.state, f"failed to reach the state {actual_column_information.state}"
#     assert actual_column_information.current_temperature == expected_column_information.current_temperature, f"failed to reach the current temperature {actual_column_information.current_temperature}"


# def build_column_information(action, column_id, set_point, state, target_temperature):
#     """
#     This function returns the expected value of the parameter that needs to be validate
#     @param action:
#     @param column_id:
#     @param set_point:
#     @param state:
#     @param target_temperature:
#     @return:
#     """
#     expected_column_information = ColumnInfo()
#     expected_column_information.action = action
#     expected_column_information.resource_id = column_id
#     expected_column_information.state = state
#     expected_column_information.set_point = set_point
#     expected_column_information.current_temperature = target_temperature
#     return expected_column_information


# def extract_column_information(column_id, response_column_info_list):
#     """
#     This function extracts the information from the response of the info api for each column
#     @param column_id:
#     @param response_column_info_list:
#     @return:
#     """
#     index = 0
#     while index < len(response_column_info_list):
#         if response_column_info_list[index].resource_id == column_id:
#             return response_column_info_list[index]
#         index += 1
#     return None


# def invoke_column_info() -> ColumnManagerInfoResponse:
#     """
#     This function creates request for the info api and returns the response
#     @return: ColumnManagerInfoResponse
#     """
#     url = UrlBuilder().get_api_url("column_manager_info_url")
#     payload = ""
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Get, pay_load=payload,
#                              response_type=ColumnManagerInfoResponse)
#     column_manager_response = api_request.submit()
#     return column_manager_response


# def validate_initial_column_information_after_action_on(action, column_id, target_temperature):
#     """
#     This function checks for cooling or heating state depending upon the current temperature when the control action is "ON"
#     after clearing the error
#     @param action:
#     @param column_id:
#     @param target_temperature:
#     @return:
#     """

#     column_manager_info = invoke_column_info()
#     response_column_info_list = column_manager_info.column_list
#     for response_column_info in response_column_info_list:
#         if response_column_info.resource_id == column_id:
#             current_temperature = response_column_info.current_temperature
#             if current_temperature <= target_temperature:
#                 assert response_column_info.state == ColumnManagerStates.Heating \
#                        or response_column_info.state == ColumnManagerStates.AtTarget
#                 logger.info(" **********************Column Current State: Heating****************")
#             else:
#                 assert response_column_info.state == ColumnManagerStates.Cooling \
#                        or response_column_info.state == ColumnManagerStates.AtTarget
#                 logger.info(" **********************Column Current State: cooling ****************")




