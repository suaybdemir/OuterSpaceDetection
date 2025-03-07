using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using OuterSpaceDetection.WebApi.Domain.Entities;

namespace OuterSpaceDetection.WebApi.Infrastructure.Configurations;

public sealed class SpaceObjectConfiguration : IEntityTypeConfiguration<SpaceObject>
{
    public void Configure(EntityTypeBuilder<SpaceObject> builder)
    {
        builder.Property(p => p.Name).HasColumnType("varchar(50)");
    }
}
