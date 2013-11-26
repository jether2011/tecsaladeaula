from core.models import Course, CourseProfessor, CourseStudent, Lesson, Video
from accounts.serializers import TimtecUserSerializer
from rest_framework import serializers


class CourseProfessorSerializer(serializers.ModelSerializer):
    user = TimtecUserSerializer()

    class Meta:
        model = CourseProfessor


class CourseStudentSerializer(serializers.ModelSerializer):
    user = TimtecUserSerializer()

    class Meta:
        model = CourseStudent


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'desc', 'slug', 'name', 'units')


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'name', 'youtube_id',)


class CourseSerializer(serializers.ModelSerializer):
    intro_video = VideoSerializer()

    class Meta:
        model = Course
        fields = ("id", "slug", "name", "intro_video", "application", "requirement",
                  "abstract", "structure", "workload", "pronatec", "status", "publication",
                  "professors",)
