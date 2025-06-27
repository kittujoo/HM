class StartupConstants:
    ConfiguredTestTime = 2400  # 40min
    DefaultTestTime = 780  # 13min
    Initial_composition = 0
    MinutesToSeconds = 60
    InProgressText = "In progress..."
    StartupCompleteBannerText = "Instrument Startup Complete"

    WelcomeFirstParagraph = "Use this workflow to automate priming and equilibration to prepare the system for operation."
    WelcomeListParagraph = "Use this workflow when any of these conditions apply:"
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeListParagraph]

    WelcomeListFirstPoint = "After changing the mobile phase"
    WelcomeListSecondPoint = "After changing the sample needle"
    WelcomeListThirdPoint = "After your system idles for 4 hours or more"
    expected_list_text = [WelcomeListFirstPoint, WelcomeListSecondPoint, WelcomeListThirdPoint]

    WelcomeRecommendationText = "Run this workflow when the system has been idle for more than 48 hours."
