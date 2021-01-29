@API
Feature: API testing Scenarios


  @smoke
  Scenario Outline: Simple API Response Code Validation
    When I call the Api "<API>" with the parameters "<PARAMETERS>"
    Then The response code is "200"

    Examples:
    | API      | PARAMETERS |
    | search   | NONE       |
    | get_ship | id=1       |


  @smoke @wip
  Scenario Outline: Simple API Response Schema Validation (WIP)
    When I call the Api "<API>" with the parameters "<PARAMETERS>"
    Then The response schema matches <SCHEMA_FILE>

    Examples:
    | API      | PARAMETERS | SCHEMA_FILE          |
    | search   | NONE       | Schema_search.json   |
    | get_ship | id=1       | Schema_get_ship.json |


  @smoke
  Scenario Outline: Search for ID
    When I call the Api "get_ship" with the parameters "id=<ID>"
    Then The response code is "200"

    Examples:
    | ID |
    | 1  |
    # This next scenario will produce an error
    | 2  |


  @smoke @errors
  Scenario Outline: Search for ID
    When I call the Api "get_ship" with the parameters "<PARAMETERS>"
    Then The response code is "<RESPONSE_CODE>"
    And  The response message is "<MESSAGE>"

    Examples:
    | PARAMETERS | RESPONSE_CODE | MESSAGE                                             |
    | id=2       | 404           | Not Found, This is not the ship you are looking for |
    # This will give an error on the message
    | NONE       | 500           | Imperial Server Error, Palpatine Destroyed          |

