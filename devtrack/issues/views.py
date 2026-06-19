import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import (Reporter,Issue,CriticalIssue,LowPriorityIssue)

REPORTERS_FILE = "reporters.json"
ISSUES_FILE = "issues.json"


def read_json(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r") as file:
        try:
            return json.load(file)
        except:
            return []


def write_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

@csrf_exempt
def reporters(request):

    # POST /api/reporters/
    if request.method == "POST":

        try:
            data = json.loads(request.body)

            reporter = Reporter(
                id=data["id"],
                name=data["name"],
                email=data["email"],
                team=data["team"]
            )

            reporter.validate()

            reporters = read_json(REPORTERS_FILE)

            reporters.append(reporter.to_dict())

            write_json(REPORTERS_FILE, reporters)

            return JsonResponse(
                reporter.to_dict(),
                status=201
            )

        except Exception as ex:
            return JsonResponse(
                {"error": str(ex)},
                status=400
            )

    # GET /api/reporters/
    if request.method == "GET":

        reporters = read_json(REPORTERS_FILE)

        reporter_id = request.GET.get("id")

        if reporter_id:

            for reporter in reporters:

                if str(reporter["id"]) == reporter_id:
                    return JsonResponse(reporter)

            return JsonResponse(
                {"message": "Reporter not found"},
                status=404
            )

        return JsonResponse(
            reporters,
            safe=False
        )
    
@csrf_exempt
def issues(request):

    # POST /api/issues/
    if request.method == "POST":

        try:

            data = json.loads(request.body)

            if data["priority"] == "critical":

                issue = CriticalIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            elif data["priority"] == "low":

                issue = LowPriorityIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            else:

                issue = Issue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            issue.validate()

            issues = read_json(ISSUES_FILE)

            issues.append(issue.to_dict())

            write_json(ISSUES_FILE, issues)

            response = issue.to_dict()
            response["message"] = issue.describe()

            return JsonResponse(
                response,
                status=201
            )

        except Exception as ex:

            return JsonResponse(
                {"error": str(ex)},
                status=400
            )

    # GET /api/issues/
    if request.method == "GET":

        issues = read_json(ISSUES_FILE)

        issue_id = request.GET.get("id")
        status_filter = request.GET.get("status")

        # GET /api/issues/?id=1
        if issue_id:

            for issue in issues:

                if str(issue["id"]) == issue_id:
                    return JsonResponse(issue)

            return JsonResponse(
                {"message": "Issue not found"},
                status=404
            )

        # GET /api/issues/?status=open
        if status_filter:

            filtered = [
                issue
                for issue in issues
                if issue["status"] == status_filter
            ]

            return JsonResponse(
                filtered,
                safe=False
            )

        # GET /api/issues/
        return JsonResponse(
            issues,
            safe=False
        )