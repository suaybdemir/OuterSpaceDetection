using OuterSpaceDetection.WebApi.Application.Features.Auth.Login;
using OuterSpaceDetection.WebApi.Domain.Entities;

namespace OuterSpaceDetection.WebApi.Application.Services;
public interface IJwtProvider
{
    Task<LoginCommandResponse> CreateToken(AppUser user);
}
