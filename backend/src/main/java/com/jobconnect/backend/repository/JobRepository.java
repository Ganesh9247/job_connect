package com.jobconnect.backend.repository;

import com.jobconnect.backend.entity.Job;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface JobRepository extends JpaRepository<Job, Long> {
    List<Job> findByRecruiterId(Long recruiterId);

    @Query("SELECT j FROM Job j WHERE " +
           "(:keyword IS NULL OR LOWER(j.title) LIKE LOWER(CONCAT('%', :keyword, '%')) OR LOWER(j.description) LIKE LOWER(CONCAT('%', :keyword, '%'))) AND " +
           "(:location IS NULL OR LOWER(j.location) LIKE LOWER(CONCAT('%', :location, '%'))) AND " +
           "(:jobType IS NULL OR j.jobType = :jobType) AND " +
           "(:workMode IS NULL OR j.workMode = :workMode) AND " +
           "j.status = 'ACTIVE'")
    List<Job> searchJobs(@Param("keyword") String keyword, 
                         @Param("location") String location, 
                         @Param("jobType") String jobType, 
                         @Param("workMode") String workMode);
}
