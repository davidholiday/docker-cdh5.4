#!/usr/bin/env python

import constants
import string
import json


def get_page_template():
    return string.Template("""
<!DOCTYPE html>
<html lang="en">

    <head>
        <title>foxy</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="./bootstrap.min.css">        
        <link rel="stylesheet" href="jquery.json-view.min.css">
        <link rel="stylesheet" href="foxy_custom.css" type="text/css">

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="./jquery.json-view.min.js"></script>

    </head>

    <body>

        <!-- nav bar -->
        <nav class="navbar navbar-inverse navbar-fixed-top">

            <div class="container-fluid">
                <a href="#" class="navbar-left"><img src="./cf_logo_smallest.png"></a>
                
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-2">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">&nbsp FOXY</a>              
                </div>
        
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-2">

                    <!-- search bar -->
                    <!--
                    <form class="navbar-form navbar-center" role="search">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                        <button type="submit" class="btn btn-default">Submit</button>
                    </form>
                    -->

                    <!-- right-side buttons -->
                    <ul class="nav navbar-nav navbar-right">
                        
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">CONTAINERS <span class="caret"></span></a>
                        
                            <ul class="dropdown-menu" role="menu">
                                <li><a href="#">Action</a></li>
                            </ul>
                        </li>

                        <li><a href="#">HELP</a></li>
                    </ul>
                </div>

           </div>
        </nav>

        <!-- put some space between the nav bar and the panels -->
        <div class="spacer100"></div>

        $CONTAINER_PANELS

    </body>

</html>

        """)


def get_page(containerPanels):
    # expects a list
    sep = "\n"
    containerPanelString = sep.join(containerPanels) 
    pageTemplate = get_page_template();
    page = pageTemplate.substitute(CONTAINER_PANELS = containerPanelString)
    return page



def get_container_panel_template():
    return string.Template("""  
<div class="panel $PANEL_TYPE panel-fluid"> 
    $CONTAINER_PANEL_CONTENTS 
</div>
<div class="spacer50"></div>""")



def get_container_panel(panelType, containerName, categoryToPortsDict, foxyDataDict, containerInfo):
    
    buttonType = ""
    buttonLabel = ""
    
    if containerInfo[containerName]['State']['Running'] == True:
        buttonType = "btn-danger"
        buttonLabel = "Stop"
    else:
        buttonType = "btn-success"
        buttonLabel = "Start" 

    containerPanelContents = get_container_panel_contents(containerName, 
                                                          categoryToPortsDict, 
                                                          foxyDataDict,
                                                          buttonType,
                                                          buttonLabel)

    containerPanelTemplate = get_container_panel_template()
    containerPanel = containerPanelTemplate.substitute(CONTAINER_PANEL_CONTENTS = containerPanelContents,
                                                       PANEL_TYPE = panelType)
    return containerPanel


#<h3>$CONTAINER_NAME</h3>
def get_container_panel_content_template():
    return string.Template("""
<div class="panel-heading">
    <h4>$CONTAINER_NAME</h4>
</div> 
 <div class="panel-body">
    <ul class="nav nav-pills">
        <li class="active"><a href="#ports" data-toggle="tab" aria-expanded="true">ports</a></li>
        <li class=""><a href="#info" data-toggle="tab" aria-expanded="false">info</a></li> 
        <a href="#" class="btn $BUTTON_TYPE pull-right">$BUTTON_LABEL Container</a>
    </ul>
    <div class="tab-content"> 
        $TAB_CONTENT
    </div>                 
</div>""")




def get_container_panel_contents(containerName, categoryToPortsDict, foxyDataDict, buttonType, buttonLabel):
    containerPanelContentTemplate = get_container_panel_content_template()
    containerPanelTabContent = get_container_tab_content(containerName, categoryToPortsDict, foxyDataDict)

    containerPanelContent = containerPanelContentTemplate.substitute(CONTAINER_NAME = containerName, 
                                                                     TAB_CONTENT = containerPanelTabContent,
                                                                     BUTTON_TYPE = buttonType,
                                                                     BUTTON_LABEL = buttonLabel)
    return containerPanelContent




def get_container_tab_content_template():
    return string.Template("""
<div id="ports" class="tab-pane fade in active">
    $TABLES
</div>
<div id="info" class="tab-pane fade">
    <script>
        var json = (function() {
            var json = null;
            $$.ajax({
                'async': false,
                'global': false,
                'url': "$CONTAINER_INFO_URL",
                'dataType': "json",
                'success': function (data) {
                json = data;
                }
            });
            return json;
            })();

        $$('#info').jsonView(json)
    </script>
</div> """)                  
  





def get_container_tab_content(containerName, categoryToPortsDict, foxyDataDict):
    tables = get_container_port_tables(containerName, categoryToPortsDict, foxyDataDict)
    containerInfoURL = "./json/" + containerName + "_info.json"
    tab_content_template = get_container_tab_content_template()
    tab_content = tab_content_template.substitute(TABLES = tables, CONTAINER_INFO_URL = containerInfoURL)
    return tab_content




def get_container_port_tables(containerName, categoryToPortsDict, foxyDataDict):
    containerFoxyDataDict = foxyDataDict[containerName]

    returnVal = ""

    for category, portDict in categoryToPortsDict.iteritems():
        portCategoryTable = get_container_port_category_table(category, portDict, containerFoxyDataDict)
        returnVal = returnVal + portCategoryTable

    return returnVal



def get_container_port_category_table(category, portDict, containerFoxyDataDict):
    rows = ""
    for port in portDict:
        portKey = port + constants.DOCKER_PORTS_VALUE_SUFFIX
        rows = rows + get_container_port_category_table_row(portKey, containerFoxyDataDict)
    
    tableTemplate = get_container_port_category_table_template()
    table = tableTemplate.substitute(TABLE_ROWS = rows, CATEGORY_NAME = category)
    return table




def get_container_port_category_table_template():
    return string.Template("""
<div class="page-header">
    <h4 id="$CATEGORY_NAME">$CATEGORY_NAME</h4>
</div>  
<table class="table table-striped table-hover ">
    <thead>
            <tr>
                <th>NAME</th>
                <th>EXPOSED AS</th>       
                <th>MAPPED AS</th>
                <th>ATTRIBUTES</th>
            </tr>
    </thead>
    <tbody>
        $TABLE_ROWS
    </tbody>
</table> 
<div class="spacer50"></div>""")




def get_container_port_category_table_row(port, containerFoxyDataDict):
    row_template = get_container_port_category_table_row_template(port, containerFoxyDataDict)
    foxyPort = getFoxyPort(port)
    foxyAttributeKey = foxyPort + "." +  constants.FOXY_PORT_ATTRIBUTE_KEY

    if foxyAttributeKey in containerFoxyDataDict:
        attribute = containerFoxyDataDict[foxyAttributeKey]
        html_a_fied_attributes = get_container_port_category_table_row_attribute(attribute)
        row = row_template.substitute(ATTRIBUTES = html_a_fied_attributes)
    else:
        row = row_template.substitute(ATTRIBUTES = '')



    return row






def get_container_port_category_table_row_template(port, containerFoxyDataDict):
    #print (containerFoxyDataDict)
    foxyPort = getFoxyPort(port)
    foxyPortNameKey = foxyPort + "." + constants.FOXY_PORT_NAME_KEY

    return string.Template("""
<tr>
    <td>""" + containerFoxyDataDict[foxyPortNameKey] + """</td>
    <td>""" + port + """</td>
    <td>""" + containerFoxyDataDict[constants.DOCKER_PORT_KEY][port][constants.DOCKER_PORTS_HOST_IP_KEY] + 
                """ : """ + 
                containerFoxyDataDict[constants.DOCKER_PORT_KEY][port][constants.DOCKER_PORTS_HOST_PORT_KEY] + 
                """</td>
    <td>$ATTRIBUTES </td></tr>""")






# some lists have the '/tcp' tag on the port and some don't 
# until I get around to normalizing the data this kludge will have to do...
def getFoxyPort(port):
    return port.replace(constants.DOCKER_PORTS_VALUE_SUFFIX, '')






def get_container_port_category_table_row_attribute(attribute):
    
    returnVal = ""
    #for attribute in attributes:
    #    print attribute + " " + attributes
    if (attribute == constants.FOXY_WEB_ATTRIBUTE):
        returnVal = returnVal + """<span class="btn btn btn-success">""" + \
                              str(attribute) + \
                              """</span>"""
    else: 
        returnVal = returnVal + """<span class="label label label-warning">""" + \
                              str(attribute) + \
                              """</span>"""

    return returnVal




















