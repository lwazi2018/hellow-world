Feature: Test and navigate to the home page


  Scenario: Homepage can navigate to the register form
    Given I am on the home page
    When I can click register button class "btn-primary"
    And I can enter my name with id "firstName"
    Then I can enter my surname with  id "lastName"
    And I can enter my email address with id "emailAddress"
    And I can enter my mobile number with id "mobileNumber"
    And I accept terms and condition with name "terms_and_conditions"
    And I click get started button with a css selector "[type=submit]"
    #Then I am on the driver screen
    When I can enter my ID number with id "idNumber"
    And I will click continue button with a class "btn-primary"
    And I enter my vehicle licence number with id "licNumber"
    And I click continue button using css selector "[type=submit]"
    And The dropdown is found by a class "fa-chevron-down" in i tag
    And This is my vehicle button is found by a id "my-car-button" selector
    And Current vehicle condition is selected by id "radio-condition-poor" "radio-condition-good" "radio-condition-very_good" selector
    And My current vehicle mileage is "rz-pointer"
    And Enter a model year of your vehicle with id "year"
    #And Click yes in is the vehicle financed question by an css selector "[type=radio]"
    And Select licence year of the user with an id "first_licence_year"
    And Click continue button to go to the next page by css selector "button[type=submit]"
    And Manually configure your vehicle info on the next page id "make" "model_obj" "year" "button[type=submit]"
    And Click continue button after a manual process to go to the next page by css selector "cont-button"
    And Click user my current location link by id "vehicle-loc" "content"
    And Click continue button on a vehicle page to user frequency using id "loc-cont-button"
    And Scroll the slider and select days you drive your car per week "rz-pointer"
    And Deselect and select working days "[value=Monday]" "[value=Tuesday]" "[value=Wednesday]" "[value=Thursday]" "[value=Friday]" "[value=Saturday]" "[value=Sunday]" "button[type=submit]"
    And Assert we're almost there page then click let's do this "get_quote_link"
    And Click continue on the base premium page "base-button"
    And Click yes to accept theft and hijack cover "theft-id"
    And Click yes to accept natural causes cover "natural_causes_id"
    And Click yes to accept a total write off cover "total_write_off_id"
    And Click got it button to accept a quote reminder "got_it_id" and click accept "accept_id"
    And Set the user password and confirm it "password" confirm "passwordConfirm" the continue "button[type=submit]"
    And Enter user banking details "bank" "account_type" "accName" "accNumber" "branchCode" "payment_cont_button"
    And Click continue to accept telematics installation "telematics_id"
    And Click maybe later link on invite friend page "maybe_later_id"
    And Click take to my dashboard to access your dashboard "take_me_to_dashboard"
    Then I log out of the system with id "logout"
    #Given I can see login button from the home page
    When I click login button log in form opens "login"
    Then Enter email and password "emailInput" "passwordInput"
    And Click click log in button "loginButton"
    When I click user profile on the dashboard it should open profile page "profileName"
    Given User want to update their profile
    Then Enter new information "firstName" "lastName" "mobileNumber"
    And Update user banking details "bank" "account_type" "other_bank" "accName" "accNumber" "branchCode"
    And Update user emergency contact "contactFullName" "contactPhoneNumber"
    Then Click update and save button link "updateAndSave"
    And Click products from the left side menu "product_id"
    Given User wants to view their products
    When user wants to activate their theft and hijack cover "activate-cover" "continueToPause"
    And user click their dashboard "dashboard-id"
    Given I want to view my driving tips from my dashboard by clicking driving tips link
    And Click driving tips to view your driving tips "driving-tips-id"











