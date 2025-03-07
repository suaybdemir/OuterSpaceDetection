using AutoMapper;
using OuterSpaceDetection.WebApi.Application.Services;
using OuterSpaceDetection.WebApi.Domain.Dtos;
using OuterSpaceDetection.WebApi.Domain.Entities;

namespace OuterSpaceDetection.WebApi.Infrastructure.Services;

public sealed class SpaceObjectClassifier : ISpaceObjectClassifier
{
    private readonly IOpenCVService _openCVService;
    private readonly IMapper _mapper;
    public SpaceObjectClassifier(IOpenCVService openCVService, IMapper mapper)
    {
        _openCVService = openCVService;
        _mapper = mapper;
    }
    public async Task<SpaceObjectDto> ClassifyStarAsync(string imagePath, CancellationToken cancellationToken)
    {
        var image = await _openCVService.ProcessImageAsync(imagePath, cancellationToken);
        // Star'ı analiz et ve döndür

        var spaceObject = _mapper.Map<SpaceObjectDto>(image);
        return spaceObject;
    }
}
