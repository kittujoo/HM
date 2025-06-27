# """
# File_Name: test_prime_solvent.py
# Desc: This file contains the step definitons for the prime solvent tests
# __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 08/19/2020

# """
# import time
# from pytest_bdd import scenarios, given, when, then
# from Kiosk.tests.Apis.Request.QSM.PrimeSolvent.prime_solvent_start_request import PrimeByTime, SolventRequest, \
#     PrimeByComposition, \
#     PrimeEndCondition, PrimeSolventStartRequest
# from isym_test_api.rest_api.api.api_request import ApiRequest
# from isym_test_api.rest_api.api.api_request_type import ApiRequestType
# from Kiosk.tests.Apis.Responses.QSM.PrimeSolvent.prime_solvent_info_response import PrimeInfoResponse, List, \
#     Solvent
# from webframework.kiosk.common.Constants.Api.prime_solvent import PrimeSolventErrorCodes, PrimeSolventConstants, PrimeSolventStates
# from utilities.logger import Logger
# from webframework.kiosk.common.Utilities.url_builder import UrlBuilder
# scenarios('../../../features/QSM/prime_solvent.feature')
# logger = Logger("test_prime_solvent")

# ### This test file needs lot of work in regards to mechanism used to assert with maxTimeToWait condition.
# ## ifthis file is to used in future, the following list needs to be completed
# #TODO 1) Instead of count while waiting for the condition we need to use a  more robust mechanism like "assert time.time() - start_time <= max_time".
# #TODO 2) method names in TypeConverter class (to be clearer on what each method does).
# #TODO 3) better comments, docstrings for the response and request class related to the prime solvent tests

# def invoke_base_api(url, api_name, payload):
#     headers = {"Content-Type": "application/json"}
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     logger.info(f" {api_name} response  => {response}")
#     assert (response.message, response.error_code) == ("ok", PrimeSolventErrorCodes.NoError), \
#         f"Failed to {api_name} message {response.message} error_code {response.error_code}"


# @given('Initial setup for the prime solvent')
# def initial_set_up():
#     url = UrlBuilder().get_api_url("prime_solvent_stop_url")
#     api_name = "clear_alarm"
#     payload = ""
#     invoke_base_api(url, api_name, payload)
#     info_url = UrlBuilder().get_api_url("qsm_prime_solvent_info_url")
#     prime_solvent_info_request = ApiRequest(url=info_url, request_type=ApiRequestType.Get,
#                                             response_type=PrimeInfoResponse)
#     # TODO 1) Instead of count while waiting for the condition we need to use a  more robust mechanism like "assert time.time() - start_time <= max_time".
#     count = 0
#     while True:

#         prime_solvent_info_response = prime_solvent_info_request.submit()
#         time.sleep(1)
#         count = count + 1

#         if prime_solvent_info_response.data.state == PrimeSolventStates.Ready:
#             logger.info(
#                 f"******* The  initial state of prime solvents =>    {prime_solvent_info_response.data.state} ***********")
#             break

#         assert count <= 2, "Waited too long for the state to get ready "
#     logger.info('\n*********************The test starts for the prime solvent*************************************')

# @when(
#     'Request start prime by time method <prime_by_time_lines> for <prime_duration> with <end_prime_solvent_composition> for <prime_end_duration>')
# def submit_prime_solvent_start_request(prime_by_time_lines, prime_duration, end_prime_solvent_composition,
#                                        prime_end_duration):
#     solvents = build_solvents_by_time(prime_by_time_lines, 0)
#     #TODO to use function from the typeconverter
#     prime_duration = int(prime_duration)
#     prime_end_duration = int(prime_end_duration)
#     prime_by_time = PrimeByTime(solvents, prime_duration)

#     end_prime_solvents = build_solvents_by_composition(end_prime_solvent_composition, SolventRequest)
#     prime_end_duration = int(prime_end_duration)
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)

#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_time=prime_by_time)
#     url = UrlBuilder().get_api_url("prime_solvent_start_url")
#     payload = prime_solvent_start_request.to_json_string()
#     logger.info(f" *********   prime_solvent_start_request {payload}  *****************")
#     invoke_base_api(url, 'prime_solvent_start', payload)


# @then(
#     'Validate prime by time info <prime_by_time_lines> for <prime_duration> with <end_prime_solvent_composition> for <prime_end_duration>')
# def validate_solvents_prime_by_time(prime_by_time_lines, prime_duration, end_prime_solvent_composition,
#                                     prime_end_duration):

#     prime_duration = int(prime_duration)
#     prime_end_duration = int(prime_end_duration)

#     prime_solvent_info_request = build_prime_solvent_info_request()

#     expected_solvent_requests = build_solvents_by_time(prime_by_time_lines, 100)

#     count = validate_solvents_prime__by_time_busy_state(expected_solvent_requests, prime_duration,
#                                                         prime_solvent_info_request)

#     validate_solvents_prime_completed_state(count, end_prime_solvent_composition, expected_solvent_requests,
#                                             prime_duration, prime_end_duration, prime_solvent_info_request)
#     logger.info('\n*********************The test ends for the prime solvent*************************************')


# def build_prime_solvent_info_request():
#     """
#     This function builds a request for the current prime solvent information
#     @return: prime_solvent_info_request
#     """
#     url = UrlBuilder().get_api_url("qsm_prime_solvent_info_url")
#     prime_solvent_info_request = ApiRequest(url=url, request_type=ApiRequestType.Get,
#                                             response_type=PrimeInfoResponse)
#     return prime_solvent_info_request


# def validate_solvents_prime_completed_state(count, end_prime_solvent_composition, expected_solvent_requests,
#                                             prime_duration, prime_end_duration, prime_solvent_info_request):
#     """
#     This function validates that the state of the priming action  is completed
#     @return: Void
#     """
#     expected_end_prime_solvents = build_solvents_by_composition(end_prime_solvent_composition, Solvent)
#     no_of_solvents = len(expected_solvent_requests)
#     # TODO 1) Instead of count while waiting for the condition we need to use a  more robust mechanism like "assert time.time() - start_time <= max_time".
#     while True:
#         prime_solvent_info_response = prime_solvent_info_request.submit()
#         time.sleep(1)
#         count = count + 1
#         assert count <= (prime_duration * no_of_solvents) + prime_end_duration + 2, "Waited too long"

#         if prime_solvent_info_response.data.state == PrimeSolventStates.Completed:
#             break
#     logger.info(f"Number of seconds to complete prime operation  => {count}")
#     logger.info(f"Final response for prime solvent info=> {prime_solvent_info_response}")
#     validate_solvent_percentage(prime_solvent_info_response.data.solvents, expected_end_prime_solvents)
#     assert prime_solvent_info_response.data.state == PrimeSolventStates.Completed, f"The state is not COMPLETED, actual state => " \
#                                                                                    f"{prime_solvent_info_response.data.state} "
#     assert prime_solvent_info_response.data.flow_rate == 0.5, f"The flow rate is incorrect, actual flow => " \
#                                                               f"{prime_solvent_info_response.data.flow_rate} "

#     assert prime_solvent_info_response.data.total_time == (prime_duration * no_of_solvents) + prime_end_duration, \
#         f" The total prime time exceeds, {prime_solvent_info_response.data.total_time}"


# def validate_solvents_prime__by_time_busy_state(expected_solvent_requests, prime_duration,
#                                                 prime_solvent_info_request):
#     """
#     This  function is to validate the state is busy
#     @return: Void
#     """
#     # TODO 1) Instead of count while waiting for the condition we need to use a  more robust mechanism like "assert time.time() - start_time <= max_time".
#     no_of_solvents = len(expected_solvent_requests)
#     index = 0
#     while index < no_of_solvents:
#         expected_solvent_id = expected_solvent_requests[index].lineId
#         count = 0
#         while count < prime_duration:
#             prime_solvent_info_response = prime_solvent_info_request.submit()
#             actual_solvent = get_solvent_by_id(prime_solvent_info_response.data.solvents, expected_solvent_id)
#             logger.info(f"Actual solvent => {actual_solvent}")

#             assert expected_solvent_id is not None, f"Solvent not found for the id => {expected_solvent_id}"
#             assert prime_solvent_info_response.data.state == PrimeSolventStates.Busy, \
#                 f"The state is not BUSY, actual state => {prime_solvent_info_response.data.state} "

#             time.sleep(1)
#             count = count + 1
#         index += 1
#     return count


# def build_solvents_by_time(prime_by_time_lines, percentage):
#     """
#     This function takes any string from the feature file and build into a format required for sending a request
#     prime by time method
#     @param prime_by_time_lines: line id of the solvent that is required for priming in prime by time method
#     @param percentage:
#     @return:
#     """
#     lines = prime_by_time_lines.split(",")
#     solvents = []
#     for line in lines:
#         solvent = SolventRequest(line, percentage)
#         solvents.append(solvent)
#     return solvents


# def build_solvents_by_composition(solvent_compositions_string, solvent_object_type):
#     """
#     This function takes any string from the feature file and build into a format required for sending a request
#     for prime by composition method
#     @param solvent_compositions_string: line id and their percentage composition
#     @param solvent_object_type: type of request object
#     @return:
#     """
#     solvent_composition_list = solvent_compositions_string.split(',')
#     prime_solvents = []
#     for solvent_composition in solvent_composition_list:
#         key_value_pair = solvent_composition.split('=')
#         assert len(key_value_pair) == 2, f" invalid solvent composition{solvent_composition}"
#         line_id = key_value_pair[0]
#         line_percentage = key_value_pair[1]
#         line_percentage = int(line_percentage)
#         if solvent_object_type is SolventRequest:
#             prime_solvent = SolventRequest(line_id, line_percentage)
#         else:
#             prime_solvent = Solvent(line_id, line_percentage)
#         prime_solvents.append(prime_solvent)
#     return prime_solvents


# @when(
#     'Request start prime by composition <solvent_compositions_string> for <prime_duration> with end prime condition <end_prime_solvent_composition> for <prime_end_duration>')
# def start_request_for_prime_by_composition(solvent_compositions_string, prime_duration, end_prime_solvent_composition,
#                                            prime_end_duration):
#     prime_duration = int(prime_duration)
#     prime_solvents = build_solvents_by_composition(solvent_compositions_string, SolventRequest)
#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)

#     end_prime_solvents = build_solvents_by_composition(end_prime_solvent_composition, SolventRequest)
#     prime_end_duration = int(prime_end_duration)
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)

#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     url = UrlBuilder().get_api_url("prime_solvent_start_url")
#     payload = prime_solvent_start_request.to_json_string()
#     logger.info(f" *********   prime_solvent_start_request {payload}  *****************")
#     invoke_base_api(url, 'prime_solvent_start', payload)


# @then(
#     'Validate prime info <solvent_compositions_string> for <prime_duration> with <end_prime_solvent_composition> for <prime_end_duration>')
# def validate_solvents_prime_by_composition(solvent_compositions_string, prime_duration,
#                                            end_prime_solvent_composition, prime_end_duration):
#     prime_duration = int(prime_duration)
#     prime_end_duration = int(prime_end_duration)

#     expected_prime_solvents = build_solvents_by_composition(solvent_compositions_string, Solvent)

#     prime_solvent_info_request = build_prime_solvent_info_request()

#     count = validate_solvents_prime_by_composition_busy_state(expected_prime_solvents, prime_duration,
#                                                               prime_solvent_info_request)

#     validate_solvents_prime_by_composition_completion_state(count, end_prime_solvent_composition, prime_duration,
#                                                             prime_end_duration, prime_solvent_info_request)

#     logger.info('\n*********************The test ends for the prime solvent*************************************')

# def validate_solvents_prime_by_composition_completion_state(count, end_prime_solvent_composition, prime_duration,
#                                                             prime_end_duration, prime_solvent_info_request):
#     """
#     This function validates the completion state for the prime by composition method
#     @return: Void
#     """
#     expected_end_prime_solvents = build_solvents_by_composition(end_prime_solvent_composition, Solvent)
#     while True:

#         prime_solvent_info_response = prime_solvent_info_request.submit()
#         time.sleep(1)
#         count = count + 1

#         if prime_solvent_info_response.data.state == PrimeSolventStates.Completed:
#             break
#         assert count <= (prime_duration + prime_end_duration + 2), "Waited too long"

#     logger.info(f"Number of seconds to complete prime operation  => {count}")
#     logger.info(f"Final response for prime solvent info=> {prime_solvent_info_response}")
#     validate_solvent_percentage(prime_solvent_info_response.data.solvents, expected_end_prime_solvents)
#     assert prime_solvent_info_response.data.state == PrimeSolventStates.Completed, f"The state is not COMPLETED, actual state => " \
#                                                                                    f"{prime_solvent_info_response.data.state} "
#     assert prime_solvent_info_response.data.flow_rate == PrimeSolventConstants.PrimingFlowRate, f"The flow rate is incorrect, actual flow => " \
#                                                                                                 f"{prime_solvent_info_response.data.flow_rate} "
#     assert prime_solvent_info_response.data.total_time == (
#             prime_duration + prime_end_duration), f" The total prime time exceeds, {prime_solvent_info_response.data.total_time}"


# def validate_solvents_prime_by_composition_busy_state(expected_prime_solvents, prime_duration,
#                                                       prime_solvent_info_request):
#     """
#     THIs function validates the busy state for the prime by composition method
#     @return:
#     """
#     count = 0
#     while count < prime_duration:
#         prime_solvent_info_response = prime_solvent_info_request.submit()
#         logger.info(f"Initial response for prime solvent info=> {prime_solvent_info_response}")
#         validate_solvent_percentage(prime_solvent_info_response.data.solvents, expected_prime_solvents)

#         assert prime_solvent_info_response.data.state == PrimeSolventStates.Busy, \
#             f"The state is not BUSY, actual state => {prime_solvent_info_response.data.state} "
#         time.sleep(1)
#         count = count + 1
#     return count


# @when('Validate the api throws an error when invalid solvent <prime_by_time_lines> is used for priming')
# def request_start_prime_with_error_condition(prime_by_time_lines):
#     prime_solvents = build_solvents_by_time(prime_by_time_lines, 0)
#     prime_duration = 6

#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")

#     end_prime_solvent_a = SolventRequest("A", 25)
#     end_prime_solvent_b = SolventRequest("B", 75)

#     end_prime_solvents = [end_prime_solvent_a, end_prime_solvent_b]
#     prime_end_duration = 6
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     validate_error_state(prime_solvent_start_request)


# @then('Clear the error condition in prime solvent')
# def clear_alarm():
#     url = UrlBuilder().get_api_url("prime_solvent_clear_alarm_url")
#     api_name = "clear_alarm"

#     payload = ""
#     invoke_base_api(url, api_name, payload)
#     logger.info('\n*********************The test ends for the prime solvent*************************************')

# @when('Validate the api throws an error when an invalid solvent composition <solvent_compositions_string> is applied')
# def start_prime_with_invalid_composition(solvent_compositions_string):
#     prime_duration = 6
#     prime_solvents = build_solvents_by_composition(solvent_compositions_string, SolventRequest)
#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")

#     end_prime_solvent_a = SolventRequest("A", 25)
#     end_prime_solvent_b = SolventRequest("B", 75)

#     end_prime_solvents = [end_prime_solvent_a, end_prime_solvent_b]
#     prime_end_duration = 6
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     validate_error_state(prime_solvent_start_request)

# @when(
#     'Request start <prime_by_time_lines> and <solvent_compositions_string> for <prime_duration> with end prime condition <end_prime_solvent_composition> for <prime_end_duration>')
# def start_prime_by_both_methods(prime_by_time_lines, solvent_compositions_string, prime_duration,
#                                 end_prime_solvent_composition, prime_end_duration):
#     solvents = build_solvents_by_time(prime_by_time_lines, 0)
#     prime_duration = int(prime_duration)
#     prime_end_duration = int(prime_end_duration)

#     prime_by_time = PrimeByTime(solvents, prime_duration)
#     prime_solvents = build_solvents_by_composition(solvent_compositions_string, SolventRequest)
#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")
#     end_prime_solvents = build_solvents_by_composition(end_prime_solvent_composition, SolventRequest)

#     prime_end_duration = int(prime_end_duration)
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition,
#                                                            prime_by_time=prime_by_time)
#     url = UrlBuilder().get_api_url("prime_solvent_start_url")
#     payload = prime_solvent_start_request.to_json_string()
#     logger.info(f" *********   prime_solvent_start_request {payload}  *****************")
#     invoke_base_api(url, 'prime_solvent_start', payload)

# @then(
#     'Validate info response for <prime_by_time_lines> for <prime_duration> and <solvent_compositions_string> <prime_by_composition_duration> for <prime_duration> with end prime condition <end_prime_solvent_composition> for <prime_end_duration>')
# def validate_info_for_both_methods(prime_by_time_lines, prime_duration, prime_by_composition_duration,
#                                     prime_end_duration):
#     prime_duration = int(prime_duration)
#     prime_by_composition_duration = int(prime_by_composition_duration)
#     prime_end_duration = int(prime_end_duration)
#     expected_solvent_requests = build_solvents_by_time(prime_by_time_lines, 100)
#     no_of_solvents = len(expected_solvent_requests)
#     prime_solvent_info_request = build_prime_solvent_info_request()

#     count = 0
#     while True:

#         prime_solvent_info_response = prime_solvent_info_request.submit()
#         time.sleep(1)
#         count = count + 1

#         if prime_solvent_info_response.data.state == PrimeSolventStates.Completed:
#             break
#         assert count <= (no_of_solvents * prime_duration) + prime_by_composition_duration + prime_end_duration + 2, "Waited too long"

#     assert prime_solvent_info_response.data.state == PrimeSolventStates.Completed, f"The state is not COMPLETED, actual state => " \
#                                                                                    f"{prime_solvent_info_response.data.state} "
#     assert prime_solvent_info_response.data.flow_rate == PrimeSolventConstants.PrimingFlowRate, f"The flow rate is incorrect, actual flow => " \
#                                                                                                 f"{prime_solvent_info_response.data.flow_rate} "

#     logger.info('\n*********************The test ends for the prime solvent*************************************')

# @when(
#     'Validate the api throws an error when more then 100 percent solvent composition is applied in prime end condition')
# def validate_info_end_prime_conditions():
#     solvent_a = SolventRequest("A", 25)
#     solvent_b = SolventRequest("B", 25)
#     solvent_c = SolventRequest("C", 25)
#     solvent_d = SolventRequest("D", 25)
#     prime_duration = 6

#     prime_solvents = [solvent_a, solvent_b, solvent_c, solvent_d]
#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")

#     end_prime_solvent_a = SolventRequest("A", 10.1)
#     end_prime_solvent_b = SolventRequest("B", 90)

#     end_prime_solvents = [end_prime_solvent_a, end_prime_solvent_b]
#     prime_end_duration = 6
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     validate_error_state(prime_solvent_start_request)


# def validate_error_state(prime_solvent_start_request):
#     """
#     This function validates the error condition for the given request
#     @param prime_solvent_start_request:
#     @return:
#     """
#     url = UrlBuilder().get_api_url("prime_solvent_start_url")
#     payload = prime_solvent_start_request.to_json_string()
#     headers = {"Content-Type": "application/json"}
#     logger.info(f" *********   prime_solvent_start_request {payload}  *****************")
#     api_request = ApiRequest(url=url, headers=headers, request_type=ApiRequestType.Put, pay_load=payload)
#     response = api_request.submit()
#     logger.info(f"***********Response from start request {response} ***********")
#     assert response.error_code == PrimeSolventErrorCodes.InvalidParameters, f"actual error code {response.error_code}"


# @when('Validate system throws error when the user primes at <flow_rate> lower than that set in the configuration')
# def request_start_prime_with_error_condition(flow_rate):
#     solvent_a = SolventRequest("A", 25)
#     solvent_b = SolventRequest("B", 25)
#     solvent_c = SolventRequest("C", 25)
#     solvent_d = SolventRequest("D", 25)

#     prime_solvents = [solvent_a, solvent_b, solvent_c, solvent_d]

#     prime_duration = 6
#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")

#     end_prime_solvent_a = SolventRequest("A", 25)
#     end_prime_solvent_b = SolventRequest("B", 75)

#     end_prime_solvents = [end_prime_solvent_a, end_prime_solvent_b]
#     prime_end_duration = 6
#     flow_rate = float(flow_rate)
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, flow_rate, prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     validate_error_state(prime_solvent_start_request)


# @when('Validate the api throws an error when invalid solvent <prime_by_time_lines> is used for priming')
# def request_start_prime_with_error_condition(prime_by_time_lines):
#     prime_solvents = build_solvents_by_time(prime_by_time_lines, 0)
#     prime_duration = 6

#     prime_by_composition = PrimeByComposition(prime_solvents, prime_duration)
#     prime_by_composition_json = prime_by_composition.to_json_string()
#     logger.info(f"*******    prime time json {prime_by_composition_json} ***********")

#     end_prime_solvent_a = SolventRequest("A", 25)
#     end_prime_solvent_b = SolventRequest("B", 75)

#     end_prime_solvents = [end_prime_solvent_a, end_prime_solvent_b]
#     prime_end_duration = 6
#     prime_end_condition = PrimeEndCondition(end_prime_solvents, PrimeSolventConstants.PrimingFlowRate,
#                                             prime_end_duration)
#     start_prime_end_step_json = prime_end_condition.to_json_string()
#     logger.info(f"******* prime end step json {start_prime_end_step_json} ***********")
#     prime_solvent_start_request = PrimeSolventStartRequest(prime_end_condition=prime_end_condition,
#                                                            prime_by_composition=prime_by_composition)
#     validate_error_state(prime_solvent_start_request)

# def get_solvent_by_id(solvents: List[Solvent], line_id) -> Solvent:
#     """
#     This function returns the solvent of the given line id
#     @param solvents: different solvent used for priming
#     @param line_id: line id of the solvent
#     @return: solvent
#     """
#     for solvent in solvents:
#         logger.info(f"&&&&& solvent => {solvent}")
#         if solvent.line_id == line_id:
#             return solvent
#     return None


# def validate_solvent_percentage(actual_solvents: List[Solvent], expected_solvents: List[Solvent]):
#     """
#     This function is to validate each solvent percentage when prime by composition request is executed
#     @param actual_solvents: number of solvents involved in the priming action
#     @param expected_solvents: expected number of solvents
#     @return:
#     """
#     for expected_solvent in expected_solvents:
#         logger.info(f"Response for solvent => {expected_solvent}")

#         actual_solvent = get_solvent_by_id(actual_solvents, expected_solvent.line_id)
#         assert expected_solvent is not None, f"Unable to find solvent for solvent id " \
#                                              f"{expected_solvent.line_id}"

#         assert expected_solvent.composite_percentage == actual_solvent.composite_percentage, \
#             f"Percentage differs actual =>{actual_solvent.composite_percentage}" \
#             f"expected =>{actual_solvent.composite_percentage}"


# def validate_solvent_hundred_percentage(actual_solvents: List[Solvent], expected_solvents: List[Solvent]):
#     """
#     This function is to validate each solvent percentage when prime by time request is executed
#     @param actual_solvents: number of solvents involved in the priming action
#     @param expected_solvents: expected number of solvents
#     @return:
#     """
#     for actual_solvent in actual_solvents:
#         logger.info(f"Response for solvent => {actual_solvent}")

#         expected_solvent = get_solvent_by_id(expected_solvents, actual_solvent.line_id)
#         assert expected_solvent is not None, f"Unable to find bottle for  bottle id " \
#                                              f"{actual_solvent.line_id}"

#         assert actual_solvent.composite_percentage == 100, f"Percentage differs{actual_solvent.composite_percentage}"


# def build_solvents_by_time(prime_by_time_lines, percentage):
#     """
#     This function is to retrieve parametric data from the feature file and return them in solvent request format for prime by time method
#     @param prime_by_time_lines: parametric data from the feature file
#     @param percentage: percentage of each solvent
#     @return:
#     """
#     lines = prime_by_time_lines.split(",")
#     solvents = []
#     for line in lines:
#         solvent = SolventRequest(line, percentage)
#         solvents.append(solvent)
#     return solvents


# def build_solvents_by_composition(solvent_compositions_string, solvent_object_type):
#     """
#     This function is to retrieve parametric data from the feature file and return them in solvent request format for prime by composition method
#     @param solvent_compositions_string: data from the feature file
#     @param solvent_object_type: request or response object type
#     @return:
#     """
#     solvent_composition_list = solvent_compositions_string.split(',')
#     prime_solvents = []
#     for solvent_composition in solvent_composition_list:
#         key_value_pair = solvent_composition.split('=')
#         assert len(key_value_pair) == 2, f" invalid solvent composition{solvent_composition}"
#         line_id = key_value_pair[0]
#         line_percentage = key_value_pair[1]
#         line_percentage = int(line_percentage)
#         prime_solvent = None
#         if solvent_object_type is SolventRequest:
#             prime_solvent = SolventRequest(line_id, line_percentage)
#         else:
#             prime_solvent = Solvent(line_id, line_percentage)
#         prime_solvents.append(prime_solvent)
#     return prime_solvents
