#!/usr/bin/env python

import constants
import string


def get_container_panel_template():
    return string.Template('''. <div class="panel $PANEL_TYPE panel-fluid"> 
                                    $CONTAINER_PANEL_CONTENTS 
                                </div>
                                <div class="spacer50"></div>''')


def get_container_panel(panelType, containerName, categoryToPortsDict, portToDataDict, containerInfo):
    
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
                                                          portToDataDict,
                                                          buttonType,
                                                          buttonLabel)

    containerPanelTemplate = get_container_panel_template()
    containerPanel = containerPanelTemplate.substitute(CONTAINER_PANEL_CONTENTS = containerPanelContents,
                                                       PANEL_TYPE = panelType)
    return containerPanel



def get_container_panel_content_template():
    return string.Template(
             '''<div class="panel-heading">
                    <h3>$CONTAINER_NAME</h3>
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
                </div>''')




def get_container_panel_contents(containerName, categoryToPortsDict, portToDataDict, buttonType, buttonLabel):
    containerPanelContentTemplate = get_container_panel_content_template()
    containerPanelTabContent = get_container_tab_content(containerName, categoryToPortsDict, portToDataDict)

    containerPanelContent = containerPanelContentTemplate.substitute(CONTAINER_NAME = containerName, 
                                                                     TAB_CONTENT = containerPanelTabContent,
                                                                     BUTTON_TYPE = buttonType,
                                                                     BUTTON_LABEL = buttonLabel)
    return containerPanelContent




def get_container_tab_content_template():
    return string.Template(
             '''<div id="ports" class="tab-pane fade in active">
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
                </div> ''')                  
  





def get_container_tab_content(containerName, categoryToPortsDict, portToDataDict):
    tables = get_container_port_tables(categoryToPortsDict, portToDataDict)
    containerInfoURL = "./json/" + containerName + "_info.json"
    tab_content_template = get_container_tab_content_template()
    tab_content = tab_content_template.substitute(TABLES = tables, CONTAINER_INFO_URL = containerInfoURL)





def get_container_port_tables(categoryToPortsDict, portToDataDict):
    returnVal = ""

    for category, portDict in categoryToPortsDict.iteritems():
        portCategoryTable = get_container_port_category_table(category, portDict, portToDataDict)
        returnVal = returnVal + portCategoryTable

    return returnVal



def get_container_port_category_table(category, portDict, portToDataDict):
    rows = ""
    for port in portDict:
        rows = rows + get_container_port_category_table_row(port, portToDataDict)
    
    tableTemplate = get_container_port_category_table_template()
    table = tableTemplate.substitute(TABLE_ROWS = rows, CATEGORY_NAME = category)
    return table




def get_container_port_category_table_template():
    return string.Template(
            """ <div class="page-header">
                    <h4 id="$CATEGORY_NAME>$CATEGORY_NAME</h4>
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
                </table> """)




def get_container_port_category_table_row(port, portToDataDict):
    row_template = get_container_port_category_table_row_template(port, portToDataDict)
    attributes = portToDataDict[FOXY_PORT_ATTRIBUTE_KEY]
    html_a_fied_attributes = get_container_port_category_table_row_attributes(attributes)
    row = row_template.substitute(ATTRIBUTES = html_a_fied_attributes)
    return row


def get_container_port_category_table_row_template(port, portToDataDict):
    print portToDataDict
    return string.Template(
             """<tr>
                <td>""" + portToDataDict[port][constants.FOXY_PORT_NAME_KEY] + """</td>
                <td>""" + port + """</td>
                <td>""" + portToDataDict[port][DOCKER_PORTS_HOST_IP_KEY] + 
                             """ : """ + 
                             portToDataDict[port][DOCKER_PORTS_HOST_PORT_KEY] + """</td>
                <td>$ATTRIBUTES /td></tr>""")





def get_container_port_category_table_row_attributes(attributes):
    
    returnVal = ""
    for attribute in attributes:
        if (attribute == FOXY_WEB_ATTRIBUTE):
            returnVal = returnVal + """<span class="button button-lg button-default">""" + \
                                  attribute + \
                                  """Default</span>"""
        else: 
            returnVal = returnVal + """<span class="label label-lg label-default">""" + \
                                  attribute + \
                                  """Default</span>"""

    return returnVal




















