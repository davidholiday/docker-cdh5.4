#!/usr/bin/env python


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
                        ${PORTS_TAB_CONTENT}
                        ${INFO_TAB_CONTENT}
                    </div>                 
                </div>
                <div class="spacer50"></div> '''  

def get_container_panel_ports_content_template():
    return  '''
            '''                  
  




