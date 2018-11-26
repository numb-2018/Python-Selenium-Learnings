Feature: Dashboard

    Scenario Outline: Components
        Given I load the website
        When I go to "Home" page
        Then I see this component "<rows>"
        Examples:
            | rows      |
            | Home      |
            | Services  |
            | Customers |
            | About Us  |
            | Careers   |

    Scenario Outline: Services
        #Given Launch the website
        When I go to "Service" page
        Then Dashboard Status shows correct values for row "<rows>"
        Examples:
            | rows                            |
            | Digital Engineering Services    |
            | Digital Web & Mobile            |
            | Digital Test Engineering        |
            | Analytics                       |
            | Security for Digital Enterprise |
            | Cloud Services                  |
            | Google Cloud                    |
            | Digital Marketing Services      |
            | Oracle Marketing Cloud          |
            | Accelerators                    |
            | eTAAP                           |
            | eDEX                            |
            | Data Security                   |
            | GDPR                            |


    Scenario: Status Refresh
        #Given I load the website
        When I go to "Services" page
        Then I scroll to element Paragraph_1

    Scenario: Customers Info
        #Given I load the website
        When I go to "customers" page
        Then verify_customer_info_page