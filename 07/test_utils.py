"""
This module has examples of texts, needed for testing
"""

txt_text = ["Some say the world will end in fire\n",
            "Some say in ice\n",
            "From what I’ve tasted of desire\n",
            "I hold with those who favor fire\n",
            "But if it had to perish twice,\n",
            "I think I know enough of hate\n",
            "To say that for destruction ice\n",
            "Is also great\n",
            "And would suffice"]

csv_text = [
    ["Last name", "First name", "SSN",
     "Test1", "Test2", "Test3", "Test4", "Final", "Grade"],
    ["Alfalfa", "Aloysius", "123-45-6789",
     "40.0", "90.0", "100.0", "83.0", "49.0", "D-"],
    ["Alfred", "University", "123-12-1234",
     "41.0", "97.0", "96.0", "97.0", "48.0", "D+"],
    ["Gerty", "Gramma", "567-89-0123",
     "41.0", "80.0", "60.0", "40.0", "44.0", "C"]
]

json_text = {"menu": {"id": "file",
                      "value": "File",
                      "popup":
                          {
                              "menuitem": [
                                  {
                                      "value": "New",
                                      "onclick": "CreateNewDoc()"
                                  },
                                  {
                                      "value": "Open",
                                      "onclick": "OpenDoc()"
                                  },
                                  {
                                      "value": "Close",
                                      "onclick": "CloseDoc()"
                                  }
                              ]
                          }
                      }
             }
