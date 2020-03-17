// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import java.util.*;
import java.util.function.Function;

public class S3DatasetComponentBlob implements ProtoType {
  public Optional<PathDatasetComponentBlob> Path;

  public S3DatasetComponentBlob() {
    this.Path = Optional.empty();
  }

  public Boolean isEmpty() {
    if (this.Path.isPresent()) {
      return false;
    }
    return true;
  }

  // TODO: not consider order on lists
  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null) return false;
    if (!(o instanceof S3DatasetComponentBlob)) return false;
    S3DatasetComponentBlob other = (S3DatasetComponentBlob) o;

    {
      Function3<PathDatasetComponentBlob, PathDatasetComponentBlob, Boolean> f =
          (x, y) -> x.equals(y);
      if (this.Path.isPresent() || other.Path.isPresent()) {
        if (!this.Path.isPresent()) return false;
        if (other.Path.isPresent()) return false;
        if (!f.apply(this.Path.get(), other.Path.get())) return false;
      }
    }
    return true;
  }

  @Override
  public int hashCode() {
    return Objects.hash(this.Path);
  }

  public S3DatasetComponentBlob setPath(Optional<PathDatasetComponentBlob> value) {
    this.Path = value;
    return this;
  }

  public S3DatasetComponentBlob setPath(PathDatasetComponentBlob value) {
    if (value == null) this.Path = Optional.empty();
    else this.Path = Optional.of(value);
    return this;
  }

  public static S3DatasetComponentBlob fromProto(
      ai.verta.modeldb.versioning.S3DatasetComponentBlob blob) {
    if (blob == null) {
      return null;
    }

    S3DatasetComponentBlob obj = new S3DatasetComponentBlob();
    {
      Function<ai.verta.modeldb.versioning.S3DatasetComponentBlob, PathDatasetComponentBlob> f =
          x -> PathDatasetComponentBlob.fromProto(blob.getPath());
      obj.Path = Utils.removeEmpty(f.apply(blob));
    }
    return obj;
  }

  public ai.verta.modeldb.versioning.S3DatasetComponentBlob.Builder toProto() {
    ai.verta.modeldb.versioning.S3DatasetComponentBlob.Builder builder =
        ai.verta.modeldb.versioning.S3DatasetComponentBlob.newBuilder();
    this.Path.ifPresent(x -> builder.setPath(x.toProto()));
    return builder;
  }

  public void preVisitShallow(Visitor visitor) throws ModelDBException {
    visitor.preVisitS3DatasetComponentBlob(this);
  }

  public void preVisitDeep(Visitor visitor) throws ModelDBException {
    this.preVisitShallow(visitor);
    if (this.Path.isPresent()) visitor.preVisitDeepPathDatasetComponentBlob(this.Path.get());
  }

  public S3DatasetComponentBlob postVisitShallow(Visitor visitor) throws ModelDBException {
    return visitor.postVisitS3DatasetComponentBlob(this);
  }

  public S3DatasetComponentBlob postVisitDeep(Visitor visitor) throws ModelDBException {
    if (this.Path.isPresent())
      this.setPath(visitor.postVisitDeepPathDatasetComponentBlob(this.Path.get()));
    return this.postVisitShallow(visitor);
  }
}