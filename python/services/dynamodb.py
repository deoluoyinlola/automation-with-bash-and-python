
#1 - Task: Create a DynamoDB table

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='DynamoDB_Python',
    KeySchema=[
        {
            'AttributeName': 'country',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'city',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'country',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'city',
            'AttributeType': 'S'
        },
    ],
     ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#2 - Task: Add 5 or more items to the table

import boto3 # importing boto3 module

dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='*************', #insert your aws_access_key_id
    aws_secret_access_key='*************') #insert your aws_secret_access_key
    

table = dynamodb.Table('DynamoDB_Python')

with table.batch_writer() as batch: #batch writing 10 items
    
    batch.put_item(
        Item={
            'country': 'Nigeria',
            'city': 'Abuja'
            }
        )
    batch.put_item(
        Item={
            'country': 'Germany',
            'city': 'Berlin'
            }
        )
    batch.put_item(
        Item={
            'country': 'Togo',
            'city': 'Lome'
            }
        )
    batch.put_item(
        Item={
            'country': 'Cambodia',
            'city': 'Kampot'
            }
        )
    batch.put_item(
        Item={
            'country': 'Ghana',
            'city': 'Accra'
            }
        )

#3 - Task: Query the table and Remove an item

import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python')

response = table.query( 
  KeyConditionExpression=Key('country').eq('Nigeria')   #Query item with "country" and "Nigeria"
)

print(response["Items"])

## remove
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python')

#delete item 
response = table.delete_item(
    Key={
        'country': 'Nigeria', 'city': 'Abuja'})
        
print(response)

#4 - Task: Delete the table
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python')

response = table.delete()