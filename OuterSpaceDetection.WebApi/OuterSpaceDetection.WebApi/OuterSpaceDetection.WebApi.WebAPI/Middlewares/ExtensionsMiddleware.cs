﻿using OuterSpaceDetection.WebApi.Domain.Entities;
using Microsoft.AspNetCore.Identity;

namespace OuterSpaceDetection.WebApi.WebAPI.Middlewares;

public static class ExtensionsMiddleware
{
    public static void CreateFirstUser(WebApplication app)
    {
        using (var scoped = app.Services.CreateScope())
        {
            var userManager = scoped.ServiceProvider.GetRequiredService<UserManager<AppUser>>();

            if (!userManager.Users.Any(p => p.UserName == "admin"))
            {
                AppUser user = new()
                {
                    UserName = "admin",
                    Email = "admin@admin.com",
                    FirstName = "Admin",
                    LastName = "Admin",
                    EmailConfirmed = true
                };

                userManager.CreateAsync(user, "1").Wait();
            }
        }
    }
}
