package com.jobconnect.backend.repository;

import com.jobconnect.backend.entity.SavedJob;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface SavedJobRepository extends JpaRepository<SavedJob, Long> {
    List<SavedJob> findByUserId(Long userId);
    boolean existsByUserIdAndJobId(Long userId, Long jobId);
}
