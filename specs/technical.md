Wed, Feb 4

f

feyruzaMember of ⁨Amshi–Adari Record⁩, ⁨SipShare⁩, ⁨Inv_team⁩ and one more

Fri, Oct 10

from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404

from Surviliance.settings import BASIC_AUTH, KIBANA_HOST
from .forms import TargetForm
from .models import Target
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from django.contrib import messages
from watchlist.models import Target
from watchlist.forms import TargetForm
from Alert.utils import build_action_with_message, build_target_create_action, build_target_create_action
import requests
import json
from django.conf import settings


def target_create(request):
    if request.method == "POST":
        form = TargetForm(request.POST, request.FILES)
        if form.is_valid():
            target = form.sav... Read more

from os import truncate
from pyexpat.errors import messages
import re
from watchlist.models import Target
import uuid
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_GET
import json
from pytz import timezone
import requests
import logging
from notifications.signals import notify 
from Alert.forms.query_creator import process_dsl_request
from Alert.models import Alert, AlertResult
# Create your views here.
from .forms import get_alert_form, ALERT_FORM_CLASSES 
from django.shortcuts import render
from .forms import get_alert_form
from .utils import get_fields_for_index_... Read more
4:34 AM

Mon, Oct 13

password 2ubuntu and log for server sudo journalctl -u data-fusion or (the name of the app) -f
5:35 AM

Thu, Oct 30

Safety Number has changed
View Safety Number

Wed, Nov 5

1000263018684
10:29 AM

Fri, Dec 12

https://grok.com/share/c2hhcmQtNA_dc8b27ec-2553-468d-bdde-fb1f13b9d444
9:12 AM

Mon, Dec 29

feyruza invited you to join “Fixing empty field choices” on ChatGPT
chatgpt.com

https://chatgpt.com/gg/v/69527d7935288194ac301a81544bd6b7?token=e88YF4kgePMUA2YWBeB4Jw
10:09 AM

Fri, Jan 2

curl -X POST http://127.0.0.1:8000/alert/api/send/ \
  -H "Content-Type: application/json" \
  -d '{"recipient_id":1,"title":"Test","severity":"low"}'
3:44 AM

curl -X POST http://127.0.0.1:8000/alert/api/send/ \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_id": "e781ffa0-5d62-490b-a6ce-e6c896363dad",
    "title": "Server Down",
    "description": "Production server unreachable",
    "severity": "critical"
  }'
3:53 AM

{% include "includes/alert_modal.html" %}

<script src="{% static 'js/alerts.js' %}"></script>

        <!-- Extra JS block for child templates -->
        {% block extra_js %}{% endblock %}
4:43 AM

{% load static %}


<header id="page-topbar">
    <div class="navbar-header">
        <div class="d-flex">
            <!-- LOGO -->


            {% if request.user.is_superuser %}
            <div class="navbar-brand-box">
                <a href="{% url 'user_management:user_management' %}"  class="logo logo-dark">
                    <span class="logo-sm">
                        <img src="{% static 'assets/images/logo-light.png' %}" alt="" height="50">
                    </span>
                    <span class="logo-lg">
                        <img src="{% static 'assets/images/logo-light.png' %}" alt="" height="50">
                    </span>
                </a>
                <a href="{% url 'user_management:user_management' %}"  class="logo logo-light">
                    <sp... Read more
4:46 AM

async function checkActiveAlert() {
    const res = await fetch("/alert/active/");
    const data = await res.json();

    const modal = document.getElementById("alert-modal");
    const sound = document.getElementById("alert-sound");

    if (!data.alert) {
        modal.style.display = "none";
        sound.pause();
        return;
    }

    const alert = data.alert;

    if (alert.severity === "high" || alert.severity === "critical") {
        document.getElementById("alert-title").innerText = alert.title;
        document.getElementById("alert-desc").innerText = alert.description;

        modal.dataset.alertId = alert.id;
        modal.style.display = "block";

        if (sound.paused) sound.play();
    }
}


async function loadNotifications() {
    const res = await fetch("/alert/n... Read more

{% load static %}

<div id="alert-modal"
     data-alert-id=""
     style="display:none;
            position:fixed;
            inset:0;
            background:rgba(0,0,0,0.65);
            z-index:1055;
            display:flex;
            align-items:center;
            justify-content:center;">

    <div class="card shadow-lg border-0"
         style="max-width:420px; width:100%; border-radius:12px;">

        <!-- Header -->
        <div class="card-header bg-danger text-white text-center">
            <h5 class="mb-0 fw-semibold">
                <i class="bx bx-error-circle me-2"></i>
                Critical Alert
            </h5>
        </div>

        <!-- Body -->
        <div class="card-body text-center p-4">
            <h4 id="alert-title" class="fw-bold text-dark mb-3"><... Read more
4:54 AM

Tue, Jan 13

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Alert

# ----------------------------
# Test view to load base page
# ----------------------------
def test_alert(request):
    return render(request, 'base.html')


# ----------------------------
# Get active alert for user
# ----------------------------
@login_required
def active_alert(request):
    # Use __in with various cases or just lowercase if we are sure it's normalized.
    # To be safe, we use __in with the most common variants.
... Read more

(function () {
    console.log("ALERTS SYSTEM INITIALIZING...");

    async function checkActiveAlert() {
        try {
            const res = await fetch("/alert/active/");
            if (!res.ok) {
                console.warn("Active alert check failed:", res.status);
                return;
            }
            const data = await res.json();

            const modal = document.getElementById("alert-modal");
            const sound = document.getElementById("alert-sound");

            if (!data || !data.alert) {
                if (modal) modal.style.display = "none";
                if (sound) sound.pause();
                return;
            }

            const alert = data.alert;
            console.log("ALERT DETECTED:", alert.title, "Severity:", alert.severity);

        ... Read more

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Alert

# ----------------------------
# Test view to load base page
# ----------------------------
def test_alert(request):
    return render(request, 'base.html')


# ----------------------------
# Get active alert for user
# ----------------------------
@login_required
def active_alert(request):
    # Use __in with various cases or just lowercase if we are sure it's normalized.
    # To be safe, we use __in with the most common variants.
... Read more
8:07 AM

from django.contrib.auth import get_user_model
from notifications.signals import notify
from .models import Alert

User = get_user_model()


def get_system_user():
    user, _ = User.objects.get_or_create(
        username="system",
        defaults={"email": "system@local"}
    )
    return user


def send_event(
    *,
    actor=None,
    recipient,
    title,
    description="",
    severity="medium",
    source="system",
    data=None,
):
    sender = actor if actor else get_system_user()

    # Normalize severity
    severity = (severity or "medium").strip().lower()

    # 🔔 Send notification
    notify_kwargs = {
        "sender": sender,
        "recipient": recipient,
        "verb": title,
        "description": description,
        "level": "error" if severity in ["high", "criti... Read more

(function () {
    console.log("ALERTS SYSTEM INITIALIZING...");

    async function checkActiveAlert() {
        try {
            const res = await fetch("/alert/active/");
            if (!res.ok) {
                console.warn("Active alert check failed:", res.status);
                return;
            }
            const data = await res.json();

            const modal = document.getElementById("alert-modal");
            const sound = document.getElementById("alert-sound");

            if (!data || !data.alert) {
                if (modal) modal.style.display = "none";
                if (sound) sound.pause();
                return;
            }

            const alert = data.alert;
            console.log("ALERT DETECTED:", alert.title, "Severity:", alert.severity);

        ... Read more
8:30 AM

Wed, Jan 14

Safety Number has changed
View Safety Number

Fri, Jan 23

@csrf_exempt
def receive_alert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        raw_body = request.body.decode("utf-8", errors="replace")
        logger.debug("RAW BODY FROM LOGSTASH: %s", raw_body)
        logger.info("📥 Received alert payload: %s", raw_body)

        # Parse JSON payload safely
        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # --- Validate alert_uuid ---
        alert_uuid_str = payload.get("alert_uuid")
        if not alert_uuid_str:
            return JsonResponse({"error": "'alert_uuid' is required"}, status=400)
        try:
            alert_uuid = uuid.UUID(aler... Read more
8:53 AM

@csrf_exempt
def receive_alert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        raw_body = request.body.decode("utf-8", errors="replace")
        logger.debug("RAW BODY FROM LOGSTASH: %s", raw_body)
        logger.info("📥 Received alert payload: %s", raw_body)

        # Parse JSON payload safely
        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # --- Validate alert_uuid ---
        alert_uuid_str = payload.get("alert_uuid")
        if not alert_uuid_str:
            return JsonResponse({"error": "'alert_uuid' is required"}, status=400)
        try:
            alert_uuid = uuid.UUID(aler... Read more
8:53 AM

# Alternative: Rename the key to avoid conflict
notification_data = {
    "context": context_obj,
    "detailed_rows": detailed_rows,
    "story": story_text,
    "targets": targets,
    "notification_severity": level,  # Renamed to avoid conflict
    "type": "watchlist" if targets else "alert",
}

# Then use it
result = send_event(
    actor=get_system_user(),
    recipient=user,
    title=f"{getattr(alert, 'alert_name', 'Alert')} triggered",
    description=target_message.strip(),
    severity=sev,
    source="elasticsearch_alert",
    data=notification_data
)
9:22 AM

@csrf_exempt
def receive_alert(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        raw_body = request.body.decode("utf-8", errors="replace")
        logger.debug("RAW BODY FROM LOGSTASH: %s", raw_body)
        logger.info("📥 Received alert payload: %s", raw_body)

        # Parse JSON payload safely
        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # --- Validate alert_uuid ---
        alert_uuid_str = payload.get("alert_uuid")
        if not alert_uuid_str:
            return JsonResponse({"error": "'alert_uuid' is required"}, status=400)
        try:
            alert_uuid = uuid.UUID(aler... Read more
9:32 AM

# alerts/models.py

from django.db import models
from django.conf import settings
import uuid

from apps.user_authentication.models import SystemUser

User = settings.AUTH_USER_MODEL

class Alert(models.Model):
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    alert_name = models.CharField(max_length=255)
    alert_message = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(SystemUser, on_delete=models.CASCADE, related_name='alerts')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.alert_name

class AlertResult(models.Model):
    alert = models.OneToOneField(
        Alert,
        to_field='alert_id',
        on_delete=models.CASCADE,
        related_name='resul... Read more
10:24 AM

notification_id = models.PositiveIntegerField(null=True, blank=True)
10:30 AM

Sat, Jan 31

output {
  # HTTP output to Django endpoint
  http {
    url => "https://192.168.6.183:8000/Alert_/receive_alert/"
    http_method => "post"

    # Send the JSON payload - NO format parameter
    message => "%{final_payload_json}"

    headers => {
      "Content-Type" => "application/json"
      "Idempotency-Key" => "%{[@metadata][idempotency_key]}"
    }

    # SSL configuration
    ssl_enabled => true
    ssl_verification_mode => "none"

    # Retry configuration
    retry_failed => true
    retry_non_idempotent => true

    # Timeout settings
    socket_timeout => 30
    connect_timeout => 10
  }
} for 
ጃንዩ 31 11:38:30 ubuntu2.niss.gov.et logstash[862060]: [2026-01-31T11:38:30,013][ERROR][logstash.outputs.http    ][main][799a935ddb34938ba83a1431aaf51958f29ec701bc2c1e338f8938ebec7871d9]... Read more
8:39 AM

/docker-entrypoint.d/15-local-resolvers.envsh
datafusion_nginx    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
datafusion_nginx    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
datafusion_nginx    | /docker-entrypoint.sh: Configuration complete; ready for start up
datafusion_nginx    | nginx: [warn] the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/conf.d/default.conf:15
datafusion_django   | [2026-01-31 09:01:41,613] WARNING django.request: Not Found: /alert/notifications/
datafusion_django   | [2026-01-31 09:01:45,621] WARNING django.request: Not Found: /alert/active/
datafusion_django   | [2026-01-31 09:01:45,621] WARNING django.request: Not Found: /alert/notificati... Read more
9:13 AM

Wed, Feb 4

{
	"servers": {
		"tenxfeedbackanalytics": {
			"url": "https://mcppulse.10academy.org/proxy",
			"type": "http",
             "headers": {
                "X-Device": "windows",
                "X-Coding-Tool": "vscode"
            }
		}
	},
	"inputs": []
}
11:02 AM

docx

Project_Chimera_Agent_Social_Network_Analysis.docx
38 kB
11:29 AM

1 Unread Message
Today

# Technical Specification

## Architecture Overview
- Backend: Django
- Analytics Engine: Elasticsearch
- Agents communicate via JSON-based contracts
- Reports generated as JSON, HTML, or PDF

---

## API Contracts

### Agent Task Request
```json
{
  "task_id": "uuid",
  "agent_type": "planner | worker | judge",
  "input": {
    "query": "string",
    "filters": {},
    "time_range": {
      "from": "ISO-8601",
      "to": "ISO-8601"
    }
  }
}


---

## JSON Schemas

### Agent Task Request (JSON Schema)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AgentTaskRequest",
  "type": "object",
  "required": ["task_id", "agent_type", "input"],
  "properties": {
    "task_id": {"type": "string", "format": "uuid"},
    "agent_type": {"type": "string", "enum": ["planner", "worker", "judge"]},
    "input": {
      "type": "object",
      "properties": {
        "query": {"type": "string"},
        "filters": {"type": "object"},
        "time_range": {
          "type": "object",
          "properties": {
            "from": {"type": "string", "format": "date-time"},
            "to": {"type": "string", "format": "date-time"}
          },
          "required": ["from", "to"]
        }
      },
      "required": ["query", "time_range"]
    }
  }
}
```

### Trend Result (JSON Schema)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TrendResult",
  "type": "object",
  "required": ["platform", "topic", "trend_score", "timestamp"],
  "properties": {
    "platform": {"type": "string"},
    "topic": {"type": "string"},
    "trend_score": {"type": "number"},
    "timestamp": {"type": "string", "format": "date-time"}
  }
}
```

---

## Data Storage & DB Schema

Primary analytical store: **Elasticsearch** (time-series, high-cardinality video metadata).

Recommended index: `video_metadata_v1`

Example Elasticsearch mapping (minimal):
```json
{
  "mappings": {
    "properties": {
      "video_id": {"type": "keyword"},
      "platform": {"type": "keyword"},
      "title": {"type": "text"},
      "description": {"type": "text"},
      "published_at": {"type": "date"},
      "views": {"type": "long"},
      "likes": {"type": "long"},
      "tags": {"type": "keyword"},
      "geo": {"type": "geo_point"},
      "category": {"type": "keyword"},
      "ingest_timestamp": {"type": "date"}
    }
  }
}
```

Notes:
- Use `keyword` for fields used in aggregations (platform, tags, category).
- Use `date` fields with proper timezone-normalized ISO-8601.
- Create time-based index rotation (monthly/daily) depending on ingest volume.

Relational fallback / metadata catalog (ERD stub):

- Table: `videos`
  - `id` (pk, uuid)
  - `platform` (varchar)
  - `video_id` (varchar)
  - `title` (text)
  - `published_at` (timestamp)
  - `ingest_timestamp` (timestamp)

- Table: `video_metrics` (time series)
  - `id` (pk)
  - `video_id` (fk -> videos.id)
  - `metric_ts` (timestamp)
  - `views` (bigint)
  - `likes` (bigint)

Use PostgreSQL for low-volume, strongly consistent use-cases; prefer Elasticsearch for analytics and high-cardinality aggregations.

---

## Indexing & Retention

- Retention policy: keep raw events 90 days, rollup monthly aggregates to long-term store.
- Create ILM (Index Lifecycle Management) policies in Elasticsearch to automate rollover and deletion.

