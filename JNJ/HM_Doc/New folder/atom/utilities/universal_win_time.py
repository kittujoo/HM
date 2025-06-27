import subprocess
import os
from datetime import datetime, timedelta
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class WindowsTimeManagement:
    """Common Windows time management class"""

    @staticmethod
    def modify_system_time(year=0, month=0, day=0, hours=0, minutes=0, seconds=0):
        """
        Modifies the system time by adding or subtracting the specified duration to the current time.

        Parameters:
        - year (int): Number of years to add or subtract.
        - month (int): Number of months to add or subtract.
        - day (int): Number of days to add or subtract.
        - hours (int): Number of hours to add or subtract.
        - minutes (int): Number of minutes to add or subtract.
        - seconds (int): Number of seconds to add or subtract.

        Example:
        WindowsTimeManagement.modify_system_time(year=1, month=2, day=3, hours=4, minutes=30, seconds=15)
        """
        try:
            # Get the current time
            current_time = datetime.now()

            # Calculate the new time by adding or subtracting the specified duration
            delta = timedelta(
                days=day,
                hours=hours,
                minutes=minutes,
                seconds=seconds,
                weeks=year * 52 + month * 4  # Assume 1 year = 52 weeks, 1 month = 4 weeks
            )
            new_time = current_time + delta

            # Format the new time in the required PowerShell format
            formatted_time = new_time.strftime('%m/%d/%Y %H:%M:%S')

            # Construct the PowerShell command to set the system time
            powershell_command = f"Set-Date '{formatted_time}'"

            # Use subprocess to execute the PowerShell command
            subprocess.run(["powershell", "-Command", powershell_command], check=True)

            logger.info(f"System time modified successfully. New time: {new_time}")
        except Exception as e:
            logger.error(f"Error modifying system time: {e}")