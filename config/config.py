import sys
sys.path.insert(0, '../')
sys.path.insert(0, '../config')
sys.path.insert(0, '../helpers')
sys.path.insert(0, '../testCases')
sys.path.insert(0, '../testSuites')
sys.path.insert(0, '../core')
sys.path.insert(0, '../core/emailHandler')
sys.path.insert(0, '../core/testRunners')

TIMEOUT = 30

# Credentials
LOGIN = 'admin'
PASSWORD = 'Austurstraeti18'
LOGIN_WRONG = 'wrongLogin'
PASSWORD_WRONG = 'wrongP'

# Urls
BASIC_URL = 'https://traceabilit-webapp-stage.azurewebsites.net'

# Suffixes
LOGIN_URL_SUFFIX = '/login'
ADMIN_URL_SUFFIX = '/admin'
CREATE_URL_SUFFIX = '/create'
FISH_BROKER_URL_SUFFIX = '/fish-broker'
SPECIES_URL_SUFFIX = '/admin/species'
USERS_URL_SUFFIX = '/admin/users'
PRODUCTS_URL_SUFFIX = '/admin/products'
VESSELS_URL_SUFFIX = '/admin/vessels'
RECIPES_URL_SUFFIX = '/admin/recipes'
PRODUCERS_URL_SUFFIX = '/admin/producers'
AIRLINES_URL_SUFFIX = '/admin/airlines'
HARBOURS_URL_SUFFIX = '/admin/harbours'
OWNERS_URL_SUFFIX = '/admin/owners'
RETAILERS_URL_SUFFIX = '/admin/retailers'
DISTRIBUTORS_URL_SUFFIX = '/admin/distributors'
DESTINATIONS_URL_SUFFIX = '/admin/destinations'
IMAGES_URL_SUFFIX = '/admin/images'


# Elements ids
LOGIN_INPUT_ID = 'mat-input-0'
PASSWORD_INPUT_ID = 'mat-input-1'
LOGIN_ERROR_MESSAGE_ID = 'mat-error-2'

# Elements xpaths
LOGIN_BUTTON_XPATH = '/html/body/app-root/div/app-login/div/div[2]/div/mat-card/mat-card-content/button'
LOGOUT_BUTTON_XPATH = '//*[@id="navbarsExampleDefault"]/button'
SPECIES_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[2]/a'
USERS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[3]/a'
PRODUCTS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[4]/a'
VESSELS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[5]/a'
RECIPES_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[6]/a'
PRODUCERS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[7]/a'
AIRLINES_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[8]/a'
HARBOURS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[9]/a'
OWNERS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[10]/a'
RETAILERS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[11]/a'
DISTRIBUTORS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[12]/a'
DESTINATIONS_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[13]/a'
IMAGES_BUTTON_XPATH =  '/html/body/app-root/div/app-admin/div/div/div[1]/app-side-menu/nav/ul/li[14]/a'
CREATE_BUTTON_XPATH = '/html/body/app-root/div/app-admin/app-toolbar/nav/div/ul/li[2]/a'
FISHBROKER_BUTTON_XPATH = '/html/body/app-root/div/app-admin/app-toolbar/nav/div/ul/li[3]/a'
HEADER_XPATH = '/html/body/app-root/div/app-login/div/div[1]/div/div/h1'
LOGO_XPATH = '/html/body/app-root/div/app-admin/app-toolbar/nav/a' # Icon TeacebiliT in top black bar

# Xpaths of Column Name in lists - Admin Panel
SPECIES_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-species/mat-table/mat-header-row/mat-header-cell[1]/div/button'
USERS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-users/mat-table/mat-header-row/mat-header-cell[1]/div/button'
PRODUCTS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-products/mat-table/mat-header-row/mat-header-cell[1]/div/button'
VESSELS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-vessels/mat-table/mat-header-row/mat-header-cell[1]/div/button'
RECIPES_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-recipes/mat-table/mat-header-row/mat-header-cell[1]/div/button'
PRODUCERS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-producers/mat-table/mat-header-row/mat-header-cell[1]/div/button'
AIRLINES_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-airlines/mat-table/mat-header-row/mat-header-cell[1]/div/button'
HARBOURS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-harbours/mat-table/mat-header-row/mat-header-cell[1]/div/button'
OWNERS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-owners/mat-table/mat-header-row/mat-header-cell[1]/div/button'
RETAILERS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-retailers/mat-table/mat-header-row/mat-header-cell[1]/div/button'
DISTRIBUTORS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-distributors/mat-table/mat-header-row/mat-header-cell[1]/div/button'
DESTINATIONS_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-destinations/mat-table/mat-header-row/mat-header-cell[1]/div/button'
IMAGES_COLUMN_HEAD = '/html/body/app-root/div/app-admin/div/div/div[2]/app-images/mat-table/mat-header-row/mat-header-cell[1]/div/button'
CREATE_SPECIES_FIELD ='/html/body/app-root/div/app-create/div/div[2]/div[1]/mat-card/mat-card-content/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'
FISHBROKER_TITLE = '/html/body/app-root/div/app-broker-dashboard/div/div[1]/div/div/h1'

# Xpaths to cloumns in Species list
SPECIES_NAME = '/html/body/app-root/div/app-admin/div/div/div[2]/app-species/mat-table/mat-row/mat-cell[1]'
SPECIES_NAME2 = '/html/body/app-root/div/app-admin/div/div/div[2]/app-species/mat-table/mat-row/mat-cell[1]'

# FILES PATHS TO TEST SORTING
RESULTS='D:/Repositories/cw-gestson-automated_tests/testCases/results.txt'
EXPECT='D:/Repositories/cw-gestson-automated_tests/testCases/expect.txt'