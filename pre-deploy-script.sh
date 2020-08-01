#!/bin/bash

pip freeze | sed -e '/pkg-resources==0.0.0/d' > requirements.txt
