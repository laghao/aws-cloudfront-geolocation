#!/bin/sh
# sed -i "s/^REGION =.*$/REGION: ${REGION}/" config.ini
# sed -i "s/^FOLDER =.*$/FOLDER: ${FOLDER}/" config.ini
# sed -i "s/^OUTPUT =.*$/OUTPUT: ${OUTPUT}/" config.ini
# sed -i "s/^DATE =.*$/DATE: ${DATE}/" config.ini
sed -i "s/^AWS_BUCKET_NAME =.*$/AWS_BUCKET_NAME: ${AWS_BUCKET_NAME}/" config.ini
sed -i "s/^AWS_ACCESS_KEY_ID =.*$/AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}/" config.ini
sed -i "s/^AWS_SECRET_ACCESS_KEY =.*$/AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}/" config.ini

python main.py