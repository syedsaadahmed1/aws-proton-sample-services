/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event from API Gateway HTTP API.
// 2. Log event and context object to CloudWatch Logs.
// 3. Send SNS message and log results to CloudWatch Logs. 
// 3. Return a response with event information and SNS message to the caller.

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 
const sns = new AWS.SNS({apiVersion: '2012-11-05'})

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event: ", JSON.stringify(event, null, 2));
    console.log("Context: ", JSON.stringify(context, null, 2));
    event.Records.forEach(record => {
      const { body } = record;
      console.log(body);
    });
    return {};
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
};