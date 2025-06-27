from datetime import datetime, timezone, timedelta, date


def current_date(format_str="%m/%d/%Y %H:%M") -> str:
    now = datetime.now(timezone.utc)
    # mm/dd/YY H:M
    dt_string = now.strftime(format_str)
    return dt_string


def is_within_tolerance(t1, t2, tolerance=5) -> bool:
    time_format = "%m/%d/%Y %H:%M"
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    time_diff = abs(time1 - time2)
    if time_diff <= timedelta(minutes=tolerance):
        return True
    return False


def is_past_event(time_1, time_2) -> bool:
    time_format = "%m/%d/%Y %H:%M"
    time_1 = datetime.strptime(time_1, time_format)
    time_2 = datetime.strptime(time_2, time_format)
    if time_1 >= time_2:
        return True
    return False


def get_date_with_days_delta(delta, format_str="%m/%d/%Y %H:%M") -> str:
    today_date = date.today()
    return (today_date - timedelta(days=delta)).strftime(format_str)


def time_convertor(expected_time, current_time) -> (str, str):
    if expected_time != '60:00':
        expected_duration = datetime.strptime(expected_time, "%M:%S")
        if 'minutes' in current_time and 'seconds' in current_time:
            actual_duration = datetime.strptime(current_time, "%M minutes %S seconds")
        elif 'minutes' in current_time:
            actual_duration = datetime.strptime(current_time, "%M minutes")
        else:
            actual_duration = datetime.strptime(current_time, "%S seconds")
        return expected_duration, actual_duration
    else:
        expected_duration = actual_duration = '60 minutes'
        return expected_duration, actual_duration
