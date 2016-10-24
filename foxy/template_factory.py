#!/usr/bin/env python

import constants



def get_container_panel_template():
	return '''<div class="panel {$PANEL_TYPE} panel-fluid"> {$CONTAINER_PANEL_CONTENTS} </div>'''


def get_container_panel_contents_template():
    return   '''<div class="panel-heading">
                    <h3>{$CONTAINER_ID}</h3>
                </div> 
                <div class="panel-body">
                    <ul class="nav nav-pills">
                        <li class="active"><a href="#ports" data-toggle="tab" aria-expanded="true">ports</a></li>
                        <li class=""><a href="#info" data-toggle="tab" aria-expanded="false">info</a></li> 
                        <a href="#" class="btn {$BUTTON_TYPE} pull-right">{$BUTTON_LABEL} Container</a>
                    </ul>
                    <div class="tab-content"> 
                        ${TAB_CONTENT}
                    </div>                 
                </div>
                <div class="spacer50"></div> '''  

def get_container_tab_content_template():
    return   '''<div id="ports" class="tab-pane fade in active">
                    <div class="page-header">
                        <h4 id="{$CATEGORY_NAME}@{$CONTAINER_ID}">{$CATEGORY_NAME}</h4>
                    </div>
                    {$TABLES}
                </div>
                <div id="info" class="tab-pane fade">
                    <script>
                        var json = (function() {
                            var json = null;
                            $.ajax({
                                'async': false,
                                'global': false,
                                'url': "./test.json",
                                'dataType': "json",
                                'success': function (data) {
                                json = data;
                            }
                        });
                        return json;
                        })();

                        $('#info').jsonView(json)
                    </script>
                </div> '''                  
  

def get_container_port_tables(categoryToPortsDict, portToDataDict):
    returnVal = ""

    for category, portDict in categoryToPortDict.itritems:
    	portCategoryTable = get_container_port_category_table(category, portDict, portToDataDict)
        returnVal = returnVal + portCategoryTable

	return returnVal



def get_container_port_category_table(category, portDict, portToDataDict):

	return """"""



def get_container_port_category_table_row_template(port, portToDataDict):
    return   """<tr>
                <td>""" + portToDataDict[port][constants.FOXY_PORT_NAME_KEY] + """</td>
                <td>""" + port + """</td>
                <td>""" + portToDataDict[port][DOCKER_PORTS_HOST_IP_KEY] + 
                             """ : """ + 
                             portToDataDict[port][DOCKER_PORTS_HOST_PORT_KEY] + """</td>
                <td>""" + {$ATTRIBUTES} + """</td>
                </tr>"""



def get_container_port_category_table_row_attributes(attributes):
    
    returnVal = ""
	for attribute in attributes:
		if (attribute == FOXY_WEB_ATTRIBUTE):
			returnVal = returnVal + """<span class="button button-lg button-default">"""
			                      + attribute 
			                      + """Default</span>"""
		else: 
			returnVal = returnVal + """<span class="label label-lg label-default">"""
			                      + attribute 
			                      + """Default</span>"""




















