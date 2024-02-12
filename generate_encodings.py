import os
import subprocess

encoding_methods = ['onehot', 'count2vec', 'alignment', 'logskeleton', 'tokenreplay', 'doc2vec', 'hash2vec', 'tfidf', 'word2vec', 'boostne', 'deepwalk', 'diff2vec', 'glee', 'grarep', 'hope', 'laplacianeigenmaps', 'netmf', 'nmfadmm', 'node2vec', 'nodesketch', 'role2vec', 'walklets']

event_folder = 'event_logs'
# Loop through each file in the event folder
for event_log in os.listdir(event_folder):
    command = f"python main.py --dataset={event_folder}/{event_log} --encoding=onehot"
    subprocess.run(command, shell=True)