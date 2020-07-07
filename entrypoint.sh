#!/bin/sh

if [[ $1 == "help" ]]; then
    echo "
    Usage:
      docker run solution <command>

      commands:
        help: This help text.

        cart-calculator --products=<products>:
            Executes the script with products listed as comma separated values.
            Available products are apple,chai,milk,oatmeal
    "

elif [[ $1 == "cart-calculator" ]]; then
    if [ -z "$2" ]; then
        echo "Please specify products."
        exit 1
    fi

    python main.py "$2"

fi