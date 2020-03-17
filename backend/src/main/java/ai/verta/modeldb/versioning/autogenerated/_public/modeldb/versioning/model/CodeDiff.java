// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import java.util.*;
import java.util.function.Function;

public class CodeDiff implements ProtoType {
  public GitCodeDiff Git;
  public NotebookCodeDiff Notebook;

  public CodeDiff() {
    this.Git = null;
    this.Notebook = null;
  }

  public Boolean isEmpty() {
    if (this.Git != null) {
      return false;
    }
    if (this.Notebook != null) {
      return false;
    }
    return true;
  }

  // TODO: not consider order on lists
  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null) return false;
    if (!(o instanceof CodeDiff)) return false;
    CodeDiff other = (CodeDiff) o;

    {
      Function3<GitCodeDiff, GitCodeDiff, Boolean> f = (x, y) -> x.equals(y);
      if (this.Git != null || other.Git != null) {
        if (this.Git == null && other.Git != null) return false;
        if (this.Git != null && other.Git == null) return false;
        if (!f.apply(this.Git, other.Git)) return false;
      }
    }
    {
      Function3<NotebookCodeDiff, NotebookCodeDiff, Boolean> f = (x, y) -> x.equals(y);
      if (this.Notebook != null || other.Notebook != null) {
        if (this.Notebook == null && other.Notebook != null) return false;
        if (this.Notebook != null && other.Notebook == null) return false;
        if (!f.apply(this.Notebook, other.Notebook)) return false;
      }
    }
    return true;
  }

  @Override
  public int hashCode() {
    return Objects.hash(this.Git, this.Notebook);
  }

  public CodeDiff setGit(GitCodeDiff value) {
    this.Git = value;
    return this;
  }

  public CodeDiff setNotebook(NotebookCodeDiff value) {
    this.Notebook = value;
    return this;
  }

  public static CodeDiff fromProto(ai.verta.modeldb.versioning.CodeDiff blob) {
    if (blob == null) {
      return null;
    }

    CodeDiff obj = new CodeDiff();
    {
      Function<ai.verta.modeldb.versioning.CodeDiff, GitCodeDiff> f =
          x -> GitCodeDiff.fromProto(blob.getGit());
      obj.Git = Utils.removeEmpty(f.apply(blob));
    }
    {
      Function<ai.verta.modeldb.versioning.CodeDiff, NotebookCodeDiff> f =
          x -> NotebookCodeDiff.fromProto(blob.getNotebook());
      obj.Notebook = Utils.removeEmpty(f.apply(blob));
    }
    return obj;
  }

  public ai.verta.modeldb.versioning.CodeDiff.Builder toProto() {
    ai.verta.modeldb.versioning.CodeDiff.Builder builder =
        ai.verta.modeldb.versioning.CodeDiff.newBuilder();
    {
      if (this.Git != null) {
        Function<ai.verta.modeldb.versioning.CodeDiff.Builder, Void> f =
            x -> {
              builder.setGit(this.Git.toProto());
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.Notebook != null) {
        Function<ai.verta.modeldb.versioning.CodeDiff.Builder, Void> f =
            x -> {
              builder.setNotebook(this.Notebook.toProto());
              return null;
            };
        f.apply(builder);
      }
    }
    return builder;
  }

  public void preVisitShallow(Visitor visitor) throws ModelDBException {
    visitor.preVisitCodeDiff(this);
  }

  public void preVisitDeep(Visitor visitor) throws ModelDBException {
    this.preVisitShallow(visitor);
    visitor.preVisitDeepGitCodeDiff(this.Git);
    visitor.preVisitDeepNotebookCodeDiff(this.Notebook);
  }

  public CodeDiff postVisitShallow(Visitor visitor) throws ModelDBException {
    return visitor.postVisitCodeDiff(this);
  }

  public CodeDiff postVisitDeep(Visitor visitor) throws ModelDBException {
    this.Git = visitor.postVisitDeepGitCodeDiff(this.Git);
    this.Notebook = visitor.postVisitDeepNotebookCodeDiff(this.Notebook);
    return this.postVisitShallow(visitor);
  }
}