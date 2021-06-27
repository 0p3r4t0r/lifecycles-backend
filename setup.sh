#!/usr/bin/env bash

# READMEN ===========================================================
: '
Run `source ./setup.sh` in order to actiave the virtual env
'


# START: GLOBAL VARIABLES ===========================================
VENV_PATH=.venv
REQUIREMENTS_DOT_TXT=requirements.txt


# START: HELPER FUNCTIONS ===========================================
activate_venv() {
    source $VENV_PATH/bin/activate
}

create_venv() {
    python3 -m venv $VENV_PATH
    activate_venv
}

update_venv() {
    pip install --upgrade pip
}

install_dependencies() {
   pip install -r $REQUIREMENTS_DOT_TXT 
}


# START: MAIN =======================================================
if [ ! -f "manage.py" ]; then
    echo "Path must be django root"
    exit 1
fi

if [ ! -d $VENV_PATH ]; then
    create_venv
fi

update_venv
activate_venv
install_dependencies
