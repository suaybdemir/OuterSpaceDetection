using AutoMapper;
using OuterSpaceDetection.WebApi.Domain.Dtos;
using OuterSpaceDetection.WebApi.Domain.Entities;

namespace OuterSpaceDetection.WebApi.Application.Mapping;
public sealed class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<SpaceObject,SpaceObjectDto>().ReverseMap();
    }
}
