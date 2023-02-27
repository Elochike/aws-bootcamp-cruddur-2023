# Week 2 — Distributed Tracing

![disttrace](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/ditributedtracing.png)

- Distributed tracing is a method of observing requests as they  advance through a distributed system. Its primary use is to profile and monitor modern applications built using microservices and (or) cloud native architecture, enabling developers to find performance issues.
**How distributed tracing works
- Distributed tracing begins with a single request. Each request is considered a trace and receives a unique ID known as a trace ID to identify that specific transaction. Traces consist of a series of tagged time intervals called spans.

- Spans represent the actual work being performed in a distributed system. Along with a name, timestamp, and optional metadata, each span also has a unique ID known as a span ID. Spans have parent-child relationships between each other that are used to show the exact path a transaction takes through the various components of an application.

- When requests move between services, all activity is recorded in the span. Once an activity is complete, the parent span refers to the child span for the next activity. Combining all these spans in the right order forms a single distributed trace that provides an overview of an entire request. Once a trace has run its course, you can search it in a presentation layer of a distributed tracing tool.

**Why do we need distributed tracing?**
- Without a way to track requests across different services, it's next to impossible to identify the service that is responsible for a performance issue. Distributed tracing provides a way to track a request from start to finish, making troubleshooting any issues faster and easier.

- Modern software architectures provide many advantages to companies. While new practices and technologies like microservices, containers, and DevOps allow teams to manage and operate their individual services more easily, they also bring new challenges. One of the biggest concerns is reduced visibility and the increased difficulty of monitoring your entire IT infrastructure.

- With modern applications, a slow-running response is distributed across several microservices and serverless functions that are monitored by multiple teams. 

- This increased complexity has prompted companies to adjust their observability strategies to provide visibility of the entire request flow, not just services in isolation.

**Distributed tracing provides observability for microservices**
- Request tracing is straightforward in a monolithic application. It aligns with application performance monitoring (APM) where a reporting tool organizes, processes, and creates visualizations of behavior from requests, helping to show how the system is performing. Developers can use these insights to quickly diagnose and resolve bottlenecks and other performance issues before they impact customer experience.

- Traditional tracing is much more challenging in a distributed system consisting of multiple services. Microservices scale independently, creating many iterations of the same function. With a monolithic application, you can trace a request through a specific function but with microservices, there could be numerous iterations of the same function, all across different servers and data centers. Distributed tracing allows you to follow requests as they move through each service.

**What is the difference between distributed tracing and logging?
- The main difference between logging and distributed tracing is that logging provides records from a single application while distributed tracing tracks requests traveling through multiple applications. Both methods help to find and debug issues by allowing you to monitor systems in real-time and look back in time to analyze previous issues.

- The rising use of microservices has introduced new complexity to software systems and by extension, system-monitoring practices. Metrics and logs lack the necessary visibility across all services to provide proper support for distributed systems.

- Logs only provide insight into the state of a single application with specific time-stamped events that took place in the system. Application performance monitoring provides a more comprehensive way to find the root cause of performance issues. Most APM tools offer some form of distributed tracing while also providing detailed diagnostic data including code-level insights and queries.

## HoneyComb

- When creating a new dataset in Honeycomb it will provide all these installation insturctions
- We'll add the following files to our `requirements.txt`

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```
- We'll install these dependencies:

```sh
pip install -r requirements.txt
```
![pipinst](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/pipinstall.PNG)

- Add to the `app.py`

```py
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```
```py
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

```py
# Initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```
![opentel](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/appopentel.PNG)


- Add the following Env Vars to `backend-flask` in docker compose

```yml
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
OTEL_SERVICE_NAME: "${HONEYCOMB_SERVICE_NAME}"
```
![OTEL](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/OTEL.PNG)

- You'll need to grab the API key from your honeycomb account:

```sh
export HONEYCOMB_API_KEY=""
gp env HONEYCOMB_API_KEY=""
```
**Acquiring a Tracer**
- To create spans, you need to get a Tracer.

from opentelemetry import trace
```
tracer = trace.get_tracer("tracer.name.here")
```
**Creating Spans**
- Now we have a tracer configured, we can create spans to describe what is happening in your application.
```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("http-handler"):
    with tracer.start_as_current_span("my-cool-function"):
        # do something
  ```
  **Adding Attributes to Spans 
```
span = trace.get_current_span()
span.set_attribute("user.id", user.id())

```
![HA](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/homeActivitiess.PNG)

- Then spin up your docker containers and make an appplication request 

**Go to Honeycomb and check the results**
- Run a query that shows Slowest traces
- Show durations of the slowest traces over the past 2 hours.
- By using a MAX(durationMs) calculation, we can identify the traces that took the longest overall. 
- it show the slowest was about 4.8 seconds


![HCgrapone](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/honeycombactivi.PNG)

![HCgraphtwo](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/secondhoneycomb.PNG)

![HCgraphthree](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/honeycombtrace.PNG)


## X-Ray

### Instrument AWS X-Ray for Flask


```sh
export AWS_REGION="ca-central-1"
gp env AWS_REGION="ca-central-1"
```

Add to the `requirements.txt`

```py
aws-xray-sdk
```

Install pythonpendencies

```sh
pip install -r requirements.txt
```

Add to `app.py`

```py
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
```

### Setup AWS X-Ray Resources

Add `aws/json/xray.json`

```json
{
  "SamplingRule": {
      "RuleName": "Cruddur",
      "ResourceARN": "*",
      "Priority": 9000,
      "FixedRate": 0.1,
      "ReservoirSize": 5,
      "ServiceName": "Cruddur",
      "ServiceType": "*",
      "Host": "*",
      "HTTPMethod": "*",
      "URLPath": "*",
      "Version": 1
  }
}
```

```sh
FLASK_ADDRESS="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"$FLASK_ADDRESS\") {fault OR error}"
```

```sh
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
```

 [Install X-ray Daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)

[Github aws-xray-daemon](https://github.com/aws/aws-xray-daemon)
[X-Ray Docker Compose example](https://github.com/marjamis/xray/blob/master/docker-compose.yml)


```sh
 wget https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.deb
 sudo dpkg -i **.deb
 ```

### Add Deamon Service to Docker Compose

```yml
  xray-daemon:
    image: "amazon/aws-xray-daemon"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_REGION: "us-east-1"
    command:
      - "xray -o -b xray-daemon:2000"
    ports:
      - 2000:2000/udp
```

We need to add these two env vars to our backend-flask in our `docker-compose.yml` file

```yml
      AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
      AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
```

### Check service data for last 10 minutes

```sh
EPOCH=$(date +%s)
aws xray get-service-graph --start-time $(($EPOCH-600)) --end-time $EPOCH
```


## CloudWatch Logs


Add to the `requirements.txt`

```
watchtower
```

```sh
pip install -r requirements.txt
```


In `app.py`

```
import watchtower
import logging
from time import strftime
```

```py
# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("some message")
```

```py
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
```

We'll log something in an API endpoint
```py
LOGGER.info('Hello Cloudwatch! from  /api/activities/home')
```

Set the env var in your backend-flask for `docker-compose.yml`

```yml
      AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
```

> passing AWS_REGION doesn't seems to get picked up by boto3 so pass default region instead


## Rollbar

https://rollbar.com/

Create a new project in Rollbar called `Cruddur`

Add to `requirements.txt`


```
blinker
rollbar
```

Install deps

```sh
pip install -r requirements.txt
```

We need to set our access token

```sh
export ROLLBAR_ACCESS_TOKEN=""
gp env ROLLBAR_ACCESS_TOKEN=""
```

Add to backend-flask for `docker-compose.yml`

```yml
ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}"
```

Import for Rollbar

```py
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
```

```py
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        rollbar_access_token,
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
```

We'll add an endpoint just for testing rollbar to `app.py`

```py
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"
```


[Rollbar Flask Example](https://github.com/rollbar/rollbar-flask-example/blob/master/hello.py)
