from pm_automation.platforms.base.views import *
from pm_automation.platforms.dashboard.serializers import *
from configurations.base_features.exceptions.base_exceptions import LocalBaseException


class PMSettingsDashboardView(PMSettingsBaseView):
    serializer_class = PMSettingsDashboardSerializer


class PMTriggerDashboardView(PMTriggerBaseView):
    serializer_class = PMTriggerDashboardSerializer


class PMIterationDashboardView(PMIterationBaseView):
    serializer_class = PMIterationDashboardSerializer
    
    def delete(self, request, pk, *args, **kwargs):
        """Override delete method to prevent deletion of default iteration"""
        # Get the iteration to check if it's the default one
        try:
            iteration = PMIteration.objects.get(id=pk)
            
            # Check if this iteration matches the PM settings' interval_value
            if iteration.interval_value == iteration.pm_settings.interval_value:
                raise LocalBaseException(
                    exception="Cannot delete the default iteration that matches the PM settings interval",
                    status_code=400
                )
            
        except PMIteration.DoesNotExist:
            raise LocalBaseException(
                exception="Iteration not found",
                status_code=404
            )
        
        return super().delete(request, pk, *args, **kwargs)


class PMIterationChecklistDashboardView(PMIterationChecklistBaseView):
    serializer_class = PMIterationChecklistDashboardSerializer


class ManualPMGenerationDashboardView(ManualPMGenerationBaseView):
    """Dashboard view for manual PM work order generation"""
    pass


