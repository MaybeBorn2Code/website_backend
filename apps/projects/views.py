# Python
from typing import (
    Any,
    Optional
)
# DRF
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
# Local
from abstracts.paginators import AbstractPaginator
from abstracts.mixins import (
    ResponseMixin,
    ObjectMixin
)
from .serializers import (
    CategoriesSerializer,
    ProjectsSerializer
)
from .models import (
    Categories,
    Projects
)


class CategoriesView(ResponseMixin, ObjectMixin, ViewSet):
    """Viewset for categories."""

    queryset = Categories.objects.all()
    paginator_class = AbstractPaginator()

    def list(self, request: Request) -> Response:
        """GET method for listing categories."""

        categories = self.queryset
        paginator = self.paginator_class
        objects = paginator.paginate_queryset(
            categories,
            request
        )
        serializer: CategoriesSerializer = \
            CategoriesSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            key_name='categories',
            data=serializer.data,
            paginator=paginator
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET method for retrieving a single category by ID."""

        category: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        if not category:
            return self.get_json_response('category not found', 'error')
        return self.get_json_response(
            {
                'title': category.title
            }
        )

    def create(self, request: Request) -> Response:
        """POST method for creating a new category."""

        serializer: CategoriesSerializer = \
            CategoriesSerializer(
                data=request.data
            )
        if not serializer.is_valid():
            return self.get_json_response('Info', 'error')
        category: Categories = serializer.save()
        return self.get_json_response(category.title, 'created successfully')

    def update(self, request: Request, pk: str) -> Response:
        """POST method for updating an existing category."""

        category: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        if not category:
            return self.get_json_response('category not found', 'error')
        serializer: CategoriesSerializer = CategoriesSerializer(
            category,
            data=request.data
        )
        if not serializer.is_valid():
            return self.get_json_response('Info', 'fail')
        serializer.save()
        return self.get_json_response('Updated', 'success')

    def destroy(self, request: Request, pk: str) -> Response:
        """DELETE method for deleting a category by ID."""

        category: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        if not category:
            return self.get_json_response('category not found', 'error')
        category.delete()
        return self.get_json_response('Category deleted', 'success')


class ProjectsView(ResponseMixin, ObjectMixin, ViewSet):
    """Viewset for projects."""

    queryset = Projects.objects.all()
    paginator_class = AbstractPaginator()

    def list(self, request: Request) -> Response:
        """GET method for listing projects."""

        projects = self.queryset
        paginator = self.paginator_class
        objects = paginator.paginate_queryset(
            projects,
            request
        )
        serializer: ProjectsSerializer = \
            ProjectsSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            key_name='projects',
            data=serializer.data,
            paginator=paginator
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET method for retrieving a single project by ID."""

        project: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        serializer: ProjectsSerializer = ProjectsSerializer(
            project
        )
        if not project:
            return self.get_json_response('project not found', 'error')
        return self.get_json_response(
            key_name='projects',
            data=serializer.data,
        )

    def create(self, request: Request) -> Response:
        """POST method for creating a new project."""

        serializer: ProjectsSerializer = \
            ProjectsSerializer(
                data=request.data
            )
        if not serializer.is_valid():
            return self.get_json_response('Error', serializer.errors)
        project: Projects = serializer.save()
        return self.get_json_response(project.title, 'created successfully')

    def update(self, request: Request, pk: str) -> Response:
        """POST method for updating an existing project."""

        project: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        if not project:
            return self.get_json_response('project not found', 'error')
        serializer: ProjectsSerializer = ProjectsSerializer(
            project,
            data=request.data
        )
        if not serializer.is_valid():
            return self.get_json_response('Info', 'fail')
        serializer.save()
        return self.get_json_response('Updated', 'success')

    def destroy(self, request: Request, pk: str) -> Response:
        """DELETE method for deleting a project by ID."""

        project: Optional[Categories] = self.get_object(
            self.queryset,
            pk
        )
        if not project:
            return self.get_json_response('project not found', 'error')
        project.delete()
        return self.get_json_response('project deleted', 'success')
