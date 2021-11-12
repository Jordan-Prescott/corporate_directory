Description:

This script runs through a file that has two values per data entry. The name and the number. 
These values simply need placing in XML format for an upload to internal services to create a new contact.

Example input:

Name,Phone Number

Example output:

<YealinkIPPhoneDirectory>
    <DirectoryEntry>
        <Name>Name</Name>
        <Telephone>Phone Number</Telephone>
    </DirectoryEntry>
</YealinkIPPhoneDirectory>

Steps:
1. Copy the input into Files/data.csv as shown in example above
2. Run the script 
3. Use the output in Files/Phonism.txt
4. Remember the next time you run this remove the data in data.csv and replace with new data
