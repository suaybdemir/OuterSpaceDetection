using MediatR;
using Microsoft.AspNetCore.Mvc;
using OuterSpaceDetection.WebApi.Application.Services;
using OuterSpaceDetection.WebApi.WebAPI.Abstractions;

namespace OuterSpaceDetection.WebApi.WebAPI.Controllers;

public class SpaceObjectsController : ApiController
{
    private readonly ISpaceObjectClassifier _spaceObjectClassifier;
    public SpaceObjectsController(IMediator mediator, ISpaceObjectClassifier spaceObjectClassifier) : base(mediator)
    {
        _spaceObjectClassifier = spaceObjectClassifier;
    }

    [HttpPost("classify")]
    public async Task<IActionResult> ClassifyStar(string imagePath,CancellationToken cancellationToken)
    {
        var star = await _spaceObjectClassifier.ClassifyStarAsync(imagePath,cancellationToken);
        return Ok(star);
    }
}
