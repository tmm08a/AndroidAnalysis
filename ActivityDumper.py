from utils import *
from androguard.misc import AnalyzeAPK

INTENT_CATEGORY="android.intent.category.VIEW"

def analyze(args, apk_queue, res_queue, output_data):
        log = Logger(args.log_file, res_queue)

        while True:
                if apk_queue.empty():
                        return
                else:
                        apk_file = apk_queue.get()
                        file_path = args.in_dir + "/" + apk_file
                        
                        log.log("Checking: %s\n" % file_path)\
                        a,d,dx = AnalyzeAPK(file_path)
                        act = ""
                        
                        for act in a.get_activities(): 
                                intent_list = a.get_intent_filters("activity",a$
                                if INTENT_CATEGORY in str(intent_list):
                                        log.log("Found an interesting activity!$
                                        log.log(act)
                                        log.log(intent_list)

                        log.log("\n\n")
                        log.flush()

