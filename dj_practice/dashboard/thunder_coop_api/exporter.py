import json
from dashboard.thunder_coop_api.serializers import NormalSerializer, Normal, BigRunSerializer, BigRun, TeamContestSerializer, TeamContest

class DataExporter:

    def export_to_json(self):
        normal_serializer = NormalSerializer(Normal.objects.all(), many=True)
        bigrun_serializer = BigRunSerializer(BigRun.objects.all(), many=True)
        teamcontest_serializer = TeamContestSerializer(TeamContest.objects.all(), many=True)

        return {
            "Normal": normal_serializer.data,
            "BigRun": bigrun_serializer.data,
            "TeamContest": teamcontest_serializer.data
        }
    
    def json_to_file(self, json_data, filepath):
        with open(filepath, 'w') as output_file:
            output_file.write(json.dumps(json_data, indent=4))
