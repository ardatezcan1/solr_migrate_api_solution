import subprocess 
import sys
import os, json

def run_command(args list):
    try:
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()

        #print (output)
        print (err)

        return_code = proc.returncode
        return return_code, output, err
    except Exception as e:
        print ("Failed to execute command - {})".format(e))
        sys.exit (1)

kinit_args = ['kinit','-kt','<keytab_full_path>','<principal>']
kinit = subprocess.Popen(kinit_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
kinitout, kiniterr = kinit.communicate()
kinitreturncode = kinit.returncode

if kiniterr:
    print("kinit failed{}".format(kiniterr))
    sys.exit(1)

start_point=0
row_range=100

for i in range(0,40):
    print(i)
    i=i+1
    putcommand = ['curl', '-k', '-g', '--negotiate', '-u:', 'https://<solr_host>:<solr_port>/solr/<source_collection_name>/select?q=*:*&start='+str(start_point)+'&rows='+str(row_range)+'&sort=<date_field>%20asc&wt=json&fl=<collection_filed1>,<collection_filed2>']
    return_code, cmd_output, cmd_error = run_command(putcommand)

    if return_code != 0:
        print("putcommand funct err - {}".format(cmd_error))
        sys.exit(1)
    else:
        json_data = json.loads(cmd_output)
        #print(json_data["response"] ["docs"])
        #print(cmd_output)
        json_dumps=json.dumps(json_data["response"] ["docs"])
    postcommand = ['curl', '-H', 'Content-Type: application/json','-k', '-g','--negotiate','-u', 'https://<solr_host>:<solr_port>/solr/<target_collection_name>/update/json/docs?commit=true', '--data-binary', str(json_dumps)]
    return_code, cmd_output, cmd_error = run_command(postcommand)

    if return_code != 0:
        print("postcommand funct err - {}".format(cmd_error))
        sys.exit(1)
    else:
        print('succesfull')
    start_point=start_point+row_range
    
