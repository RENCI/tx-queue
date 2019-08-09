xPayload='{runid: 1234}'

xJob="""
{
  "endTimestamp": "2017-07-21T17:34:28Z",
  "id": 5,
  "payload": "doi 10.5555/55555",
  "scheduledTimestamp": "2017-07-21T17:32:28Z",
  "status": "finished",
  "submitTimestamp": "2017-07-21T17:33:28Z",
  "systemRunTime": "PT1M",
  "user": "jane@gmail.com"
}
"""

xJobs="""
{
  "application/json": [
    {
      "endTimestamp": "2019-07-21T17:34:28Z",
      "id": 1,
      "payload": "doi 10.5555/55555",
      "scheduledTimestamp": "2019-07-21T17:32:28Z",
      "status": "finished",
      "submitTimestamp": "2019-07-21T17:33:28Z",
      "systemRunTime": "PT1M",
      "user": "bradley@gmail.com"
    },
    {
      "endTimestamp": "2019-08-02T11:55:30Z",
      "id": 2,
      "payload": "doi 10.5555/55555",
      "scheduledTimestamp": "2019-08-01T18:32:29Z",
      "status": "aborted",
      "submitTimestamp": "2019-08-02T10:45:30Z",
      "systemRunTime": "PT1H10M",
      "user": "bradley@gmail.com"
    },
    {
      "endTimestamp": "2019-08-02T11:55:40Z",
      "id": 3,
      "payload": "{runid: 25516}",
      "scheduledTimestamp": "2019-08-01T18:32:30Z",
      "status": "error",
      "submitTimestamp": "2019-08-02T10:35:30Z",
      "systemRunTime": "PT1H20M10S",
      "user": "tori@gmail.com"
    },
    {
      "endTimestamp": "2019-08-04T11:55:40Z",
      "id": 4,
      "payload": "{runid: 25516}",
      "scheduledTimestamp": "2019-08-01T18:32:31Z",
      "status": "finished",
      "submitTimestamp": "2019-08-02T10:35:30Z",
      "systemRunTime": "PT2D1H20M10S",
      "user": "frank@gmail.com"
    },
    {
      "endTimestamp": "",
      "id": 5,
      "payload": "{train: \"http:/github.com/path/file1\", seed:5, epochs: 5000 }",
      "scheduledTimestamp": "2019-08-01T18:32:32Z",
      "status": "running",
      "submitTimestamp": "2019-08-02T10:35:31Z",
      "systemRunTime": "",
      "user": "joan@gmail.com"
    },
    {
      "endTimestamp": "",
      "id": 6,
      "payload": "{train: \"http:/github.com/path/file2\", seed:5, epochs: 5000}",
      "scheduledTimestamp": "2019-08-01T18:32:33Z",
      "status": "queued",
      "submitTimestamp": "",
      "systemRunTime": "",
      "user": "joan@gmail.com"
    },
    {
      "endTimestamp": "",
      "id": 7,
      "payload": "{train: \"http:/github.com/path/file2\", seed:5, epochs: 5000}",
      "scheduledTimestamp": "2019-08-01T18:32:34Z",
      "status": "initializing",
      "submitTimestamp": "2019-08-02T10:35:31Z",
      "systemRunTime": "",
      "user": "joan@gmail.com"
    }
  ]
}
"""
