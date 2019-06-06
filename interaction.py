from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher('re')


@when('I can click register button class "(.*)"')
def step_impl(context, primary_class):
    button = context.browser.find_element_by_class_name(primary_class)
    button.click()


@step('I can enter my name with id "(.*)"')
def step_impl(context, first_name):
    name = context.browser.find_element_by_id(first_name)
    name.send_keys('QA')


@then('I can enter my surname with  id "(.*)"')
def step_impl(context, surname_link):
    surname = context.browser.find_element_by_id(surname_link)
    surname.send_keys('Tester')


@step('I can enter my email address with id "(.*)"')
def step_impl(context, email_link):
    email = context.browser.find_element_by_id(email_link)
    email.send_keys('lwazi+email@byteorbit.com')


@step('I can enter my mobile number with id "(.*)"')
def step_impl(context, mobile_link):
    mobile = context.browser.find_element_by_id(mobile_link)
    mobile.send_keys('0635155623')


@step('I accept terms and condition with name "(.*)"')
def step_impl(context, terms_link):
    terms = context.browser.find_element_by_name(terms_link)
    terms.click()


@step('I click get started button with a css selector "(.*)"')
def step_impl(context, reg_link):
    context.browser.save_screenshot("register_page.png")
    reg = context.browser.find_element_by_css_selector(reg_link)
    reg.click()
    context.browser.implicitly_wait(10)


@when('I can enter my ID number with id "(.*)"')
def step_impl(context, id_number):
    id_num = context.browser.find_element_by_id(id_number)
    id_num.send_keys('9904153970185')
    # import pdb; pdb.set_trace()


@step('I will click continue button with a class "(.*)"')
def step_impl(context, cont_button):
    cont_btn = context.browser.find_element_by_class_name(cont_button)
    cont_btn.click()


@step('I enter my vehicle licence number with id "(.*)"')
def step_imp(context, lic_num):
    registration_num = context.browser.find_element_by_id(lic_num)
    registration_num.clear()
    registration_num.send_keys('NRB 67815')


@step('I click continue button using css selector "(.*)"')
def step_impl(context, link_button):
    button_link = context.browser.find_element_by_css_selector(link_button)
    button_link.click()


@step('The dropdown is found by a class "(.*)" in i tag')
def step_impl(context, drop_down):
    drop = context.browser.find_element_by_class_name(drop_down)
    drop.click()
    context.browser.implicitly_wait(10)
    # import pdb;pdb.set_trace()


@step('This is my vehicle button is found by a id "(.*)" selector')
def step_impl(context, my_car_link):
    # context.browser.implicitly_wait(3)
    this_is_my_car = context.browser.find_element_by_id(my_car_link)
    context.browser.implicitly_wait(10)
    this_is_my_car.click()


@step('Current vehicle condition is selected by id "(.*)" "(.*)" "(.*)" selector')
def step_impl(context, vehicle_cond1, vehicle_cond2, vehicle_cond3):
    wait = WebDriverWait(context.browser, 15)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-pulse')))
    my_car_condition_poor = context.browser.find_element_by_id(vehicle_cond1)
    my_car_condition_good = context.browser.find_element_by_id(vehicle_cond2)
    my_car_condition_very_good = context.browser.find_element_by_id(vehicle_cond3)
    my_car_condition_poor.click()
    my_car_condition_good.click()
    my_car_condition_very_good.click()


@step('My current vehicle mileage is "(.*)"')
def step_impl(context, slider_link):
    slider_ball = context.browser.find_element_by_class_name(slider_link)
    action_chains = ActionChains(context.browser)
    action_chains.drag_and_drop_by_offset(slider_ball, 70, 0).perform()


@step('Enter a model year of your vehicle with id "(.*)"')
def step_impl(context, year_link):
    model_year = context.browser.find_element_by_id(year_link)
    model_year.clear()
    model_year.send_keys("2015")


@step('Click yes in is the vehicle financed question by an css selector "(.)"')
def step_impl(context, is_the_vehicle_financed):
    vehicle_finance = context.browser.find_element_by_css_selector(is_the_vehicle_financed)
    vehicle_finance.click()


@step('Select licence year of the user with an id "(.*)"')
def step_impl(context, lic_year):
    your_lic_year = context.browser.find_element_by_id(lic_year)
    your_lic_year.click()
    context.browser.implicitly_wait(10)
    your_lic_year = Select(context.browser.find_element_by_id(lic_year))
    your_lic_year.select_by_value('number:2018')
    context.browser.save_screenshot("vehicle_condition.png")


@step('Click continue button to go to the next page by css selector "(.*)"')
def step_impl(context, cont_link):
    cont_button = context.browser.find_element_by_css_selector(cont_link)
    context.browser.implicitly_wait(10)
    cont_button.click()


@step('Manually configure your vehicle info on the next page id "(.*)" "(.*)" "(.*)" "(.*)"')
def step_impl(context, link_make, link_model, link_model_year, cont_link):
    make = context.browser.find_element_by_id(link_make)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    make.click()
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    make = Select(context.browser.find_element_by_id(link_make))
    make.select_by_value('VOLKSWAGEN')
    model = context.browser.find_element_by_id(link_model)
    context.browser.implicitly_wait(4)
    model.click()
    context.browser.implicitly_wait(15)
    model = Select(context.browser.find_element_by_id(link_model))
    model.select_by_value('POLO 1.2 TSI HIGHLINE (2014 - 2017)')

    model_year = context.browser.find_element_by_id(link_model_year)
    model_year.send_keys('2015')
    context.browser.save_screenshot("vehicle_info.png")
    context.browser.implicitly_wait(15)
    cont_button = context.browser.find_element_by_css_selector(cont_link)
    cont_button.click()


@step('Click continue button after a manual process to go to the next page by css selector "(.*)"')
def step_impl(context, cont_link):
    cont_button = context.browser.find_element_by_id(cont_link)
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    cont_button.click()


@step('Click user my current location link by id "(.*)" "(.*)"')
def step_impl(context, current_location_link, text_content):
    my_current_location = context.browser.find_element_by_id(current_location_link)
    context.browser.implicitly_wait(10)
    my_current_location.click()
    context.browser.implicitly_wait(15)
    words = context.browser.find_elements_by_tag_name(text_content)
    # assert "Can't find your exact address? Now that's a piece of cake - just add your suburb." in words


@step('Click continue button on a vehicle page to user frequency using id "(.*)"')
def step_impl(context, cont_link):
    continue_button = context.browser.find_element_by_id(cont_link)
    context.browser.save_screenshot("vehicle_location.png")
    continue_button.click()


@step('Scroll the slider and select days you drive your car per week "(.*)"')
def step_impl(context, scroll_slider):
    slider = context.browser.find_element_by_class_name(scroll_slider)
    action_chains = ActionChains(context.browser)
    action_chains.drag_and_drop_by_offset(slider, 70, 0).perform()


@step('Deselect and select working days "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)"')
def step_impl(context, monday_link, tuesday_link, wednesday_link, thursday_link, friday_link, saturday_link,
              sunday_link, cont_link):
    monday = context.browser.find_element_by_css_selector(monday_link)
    monday.click()
    tuesday = context.browser.find_element_by_css_selector(tuesday_link)
    tuesday.click()
    wednesday = context.browser.find_element_by_css_selector(wednesday_link)
    wednesday.click()
    thursday = context.browser.find_element_by_css_selector(thursday_link)
    thursday.click()
    friday = context.browser.find_element_by_css_selector(friday_link)
    friday.click()
    saturday = context.browser.find_element_by_css_selector(saturday_link)
    saturday.click()
    sunday = context.browser.find_element_by_css_selector(sunday_link)
    sunday.click()
    # re select week days from monday to friday
    re_monday = context.browser.find_element_by_css_selector(monday_link)
    re_monday.click()
    re_tuesday = context.browser.find_element_by_css_selector(tuesday_link)
    re_tuesday.click()
    re_wednesday = context.browser.find_element_by_css_selector(wednesday_link)
    re_wednesday.click()
    re_thursday = context.browser.find_element_by_css_selector(thursday_link)
    re_thursday.click()
    re_friday = context.browser.find_element_by_css_selector(friday_link)
    re_friday.click()
    # click continue button at the bottom of the page
    button_cont = context.browser.find_element_by_css_selector(cont_link)
    button_cont.click()


@step('Assert we\'re almost there page then click let\'s do this "(.*)"')
def step_impl(context, lets_do_this_link):
    """almost_there = context.browser.find_elements_by_tag_name('h4')
    assert "We're almost there!" in almost_there
    thanks = context.browser.find_elements_by_tag_name('p')
    assert "Thanks for filling out those monstrous fields like a star!" in thanks
    ingredients = context.browser.find_elements_by_class_name('text-secondary')
    assert "Now it's time to pick your ingredients" in ingredients"""

    lets_do_this = context.browser.find_element_by_id(lets_do_this_link)
    lets_do_this.click()


@step('Click continue on the base premium page "(.*)"')
def step_impl(context, base_link):
    base_cover = context.browser.find_element_by_id(base_link)
    context.browser.implicitly_wait(10)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    base_cover.click()


@step('Click yes to accept theft and hijack cover "(.*)"')
def step_impl(context, theft_and_hijack_link):
    yes_link = context.browser.find_element_by_id(theft_and_hijack_link)
    context.browser.implicitly_wait(10)
    yes_link.click()


@step('Click yes to accept natural causes cover "(.*)"')
def step_impl(context, natural_causes_link):
    yes_link = context.browser.find_element_by_id(natural_causes_link)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    yes_link.click()


@step('Click yes to accept a total write off cover "(.*)"')
def step_impl(context, total_write_off_link):
    yes_button = context.browser.find_element_by_id(total_write_off_link)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    yes_button.click()


@step('Click got it button to accept a quote reminder "(.*)" and click accept "(.*)"')
def step_impl(context, got_it_link, accept_link):
    got_it_button = context.browser.find_element_by_id(got_it_link)
    context.browser.implicitly_wait(10)
    got_it_button.click()
    context.browser.implicitly_wait(4)
    accept_button = context.browser.find_element_by_id(accept_link)
    accept_button.click()
    context.browser.implicitly_wait(10)


@step('Set the user password and confirm it "(.*)" confirm "(.*)" the continue "(.*)"')
def step_impl(context, password_link, confirm_link, continue_link):
    password_text_field = context.browser.find_element_by_id(password_link)
    password_text_field.send_keys('Password@123')
    password_confirm = context.browser.find_element_by_id(confirm_link)
    password_confirm.send_keys('Password@123')

    continue_button = context.browser.find_element_by_css_selector(continue_link)
    continue_button.click()


@step('Enter user banking details "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)"')
def step_impl(context, bank_link, check_link, acc_name_link, acc_numb_link, branch_link, cont_button):
    bank_select = Select(context.browser.find_element_by_id(bank_link))
    bank_select.select_by_visible_text('Absa')

    account_type = context.browser.find_element_by_id(check_link)
    cheque = Select(account_type)
    cheque.select_by_visible_text('Cheque')

    holder_name = context.browser.find_element_by_id(acc_name_link)
    holder_name.send_keys('Lwazi')

    account_number = context.browser.find_element_by_id(acc_numb_link)
    account_number.send_keys('1111111111')

    branch_code = context.browser.find_element_by_id(branch_link)
    branch_code.send_keys('0000')
    context.browser.implicitly_wait(10)
    continue_button = context.browser.find_element_by_id(cont_button)
    continue_button.click()


@step('Click continue to accept telematics installation "(.*)"')
def step_impl(context, continue_button_link):
    context.browser.implicitly_wait(10)
    cont_button = context.browser.find_element_by_id(continue_button_link)
    cont_button.click()


@step('Click maybe later link on invite friend page "(.*)"')
def step_impl(context, maybe_later_link):
    context.browser.implicitly_wait(10)
    later = context.browser.find_element_by_id(maybe_later_link)
    later.click()


@step('Click take to my dashboard to access your dashboard "(.*)"')
def step_impl(context, dashboard_link):
    dashboard = context.browser.find_element_by_id(dashboard_link)
    # WebDriverWait(context.browser, 15).until(EC.invisibility_of_element_located((By.TAG_NAME, 'strong')))
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'referral-code')))
    dashboard.click()


@then('I log out of the system with id "(.*)"')
def step_impl(context, ic_logout):
    log_out = context.browser.find_element_by_id(ic_logout)
    log_out.click()


@when('I click login button log in form opens "(.*)"')
def step_impl(context, login_link):
    log_in = context.browser.find_element_by_id(login_link)
    context.browser.implicitly_wait(10)
    log_in.click()


@step('Enter email and password "(.*)" "(.*)"')
def step_impl(context, email_field, password_field):
    email = context.browser.find_element_by_id(email_field)
    email.send_keys('lwazi+email@byteorbit.com')

    password = context.browser.find_element_by_id(password_field)
    password.send_keys('Password@123')


@step('Click click log in button "(.*)"')
def step_impl(context, login_link):
    login = context.browser.find_element_by_id(login_link)
    import time
    time.sleep(0)
    login.click()


@step('I click user profile on the dashboard it should open profile page "(.*)"')
def step_impl(context, profile_link):
    context.browser.implicitly_wait(10)
    profile = context.browser.find_element_by_id(profile_link)
    profile.click()


@then('Enter new information "(.*)" "(.*)" "(.*)"')
def step_impl(context, firstname_field, lastName_field, mobileNumber_field):
    first_name = context.browser.find_element_by_id(firstname_field)
    first_name.clear()
    first_name.send_keys('Lwazi')
    last_name = context.browser.find_element_by_id(lastName_field)
    last_name.clear()
    last_name.send_keys('Tester')
    mobile_number = context.browser.find_element_by_id(mobileNumber_field)
    mobile_number.clear()
    mobile_number.send_keys('27635155623')


@step('Update user banking details "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)"')
def step_impl(context, bank_link, acc_type, other_bank_text, holder_name, acc_no, branch_code_link):
    bank_name = context.browser.find_element_by_id(bank_link)
    other = Select(bank_name)
    other.select_by_visible_text('Other')
    cheque = Select(context.browser.find_element_by_id(acc_type))
    cheque.select_by_visible_text('Cheque')
    """Write your bank that is not in the list"""
    other_bank = context.browser.find_element_by_id(other_bank_text)
    other_bank.clear()
    other_bank.send_keys('uBank')
    """Enter your name writen on your card"""
    account_holder_name = context.browser.find_element_by_id(holder_name)
    account_holder_name.clear()
    account_holder_name.send_keys('Lwazi')
    """Enter your account number"""
    account_number = context.browser.find_element_by_id(acc_no)
    account_number.clear()
    account_number.send_keys('1111111111')
    """Enter branch code for your bank"""
    branch_code = context.browser.find_element_by_id(branch_code_link)
    branch_code.clear()
    branch_code.send_keys('0000')


@step('Update user emergency contact "(.*)" "(.*)"')
def step_impl(context, emrgency_name, emergency_number):
    name = context.browser.find_element_by_id(emrgency_name)
    name.clear()
    name.send_keys('My Friend')

    number = context.browser.find_element_by_id(emergency_number)
    number.clear()
    number.send_keys('0783351995')


@then('Click update and save button link "(.*)"')
def step_impl(context, update_button):
    save_button = context.browser.find_element_by_id(update_button)
    save_button.click()


@step('Click products from the left side menu "(.*)"')
def step_impl(context, product_link):
    product = context.browser.find_element_by_id(product_link)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    product.click()


@when('user wants to activate their theft and hijack cover "(.*)" "(.*)"')
def step_impl(context, theft_link, continue_link):
    theft_and_hijack = context.browser.find_element_by_id(theft_link)
    theft_and_hijack.click()
    continue_pause = context.browser.find_element_by_id(continue_link)
    continue_pause.click()


@step('user click their dashboard "(.*)"')
def step_impl(context, dashboard_link):
    dashboard = context.browser.find_element_by_id(dashboard_link)
    WebDriverWait(context.browser, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bg')))
    dashboard.click()


@step('Click driving tips to view your driving tips "(.*)"')
def step_impl(context, driving_tips_link):
    driving_tips = context.browser.find_element_by_id(driving_tips_link)
    driving_tips.click()


@then('Read the content of your driving tips "(.*)"')
def step_impl(context, title_text):
    heading = context.browser.find_element_by_id(title_text)
    assert "Driving Tips" in heading
    import pdb;
    pdb.set_trace()
