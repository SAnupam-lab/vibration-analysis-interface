"""

Analysis API

"""

# Importing packages and modules
from fastapi import APIRouter
from sources.templates import schemas
from sources.classes.dao import DAO
from sources.classes.processing import Processing
from sources.classes.visualization import Visualization

# Setting the route
router = APIRouter(prefix="/analysis", tags=["analysis"])

# Endpoint
@router.post("/")
async def run_analysis(input: schemas.Input):
    try:
        dao = DAO(input.dataset_id, input.channel)
        sampling_frequency = dao.read_sampling_frequency()      
        samples = dao.read_samples(input.slice_start, input.slice_end)
        processing = Processing(sampling_frequency)
        processing.run(samples)
        visualization = Visualization()
        visualization.run(processing, input.figure)
        data = visualization.figure
        status = "success"
    except:
        data = None
        status = "fail"
    return {"data": data, "status": status}