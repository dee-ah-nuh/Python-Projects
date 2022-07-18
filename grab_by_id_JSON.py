# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:52:36 2022

@author: Diana Valladares
"""


{
    "limit": null,
    "query": {
        "negate": false, #remove
        "queries": [
            {
                "negate": false, #remove
                "object_type": "lead",
                "type": "object_type"
            },
            {
                "negate": false, #remove
                "queries": [#{ STARTS DICTIONARY - "queries":[                            {
                        # "condition": {
                        #     "object_ids": [
                        #         "stat_uEnaaHk6Bz2zkKST0LALLQdC2uPt9MMnl73qoeRBVBM" #PART of the CODE THAT EXTRACTS LEADS 6.0 - API KEY = CLOSE>SETTINGS>STATUSES AND PIPELINES> COPY API KEY FOR 6.0
                        #     ],
                        #     "reference_type": "status.lead",
                        #     "type": "reference"
                        # },
                        # "field": {
                        #     "field_name": "status_id",
                        #     "object_type": "lead",
                        #     "type": "regular_field"
                        # },
                        # "type": "field_condition" 
                            
"""=============================================================================
 Advanced Filtering                     
# #                         {
# #   "query": {
# #     "queries": [
# #       {
# #         "object_type": "contact",
# #         "type": "object_type",
# #       },
# #       {
# #         "type": "field_condition",
# #         "field": {
# #           "object_type": "contact",
# #           "type": "regular_field",
# #           "field_name": "title"
# #         },
# #         "condition": {
# #           "type": "text",
# #           "mode": "full_words",
# #           "value": "CEO"
# #         }
# #       }
# #     ],
# #     "type": "and"
# #   }
# # }
# =============================================================================
"""                                           
                            
                            }],
                "type": "and"
            }
        ],
        "type": "and"
    },
    "results_limit": null, #REMOVE AND ADDED __FIELDS :'_fields':{"lead":['id','custom']},

    "sort": []
}
